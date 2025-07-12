# 1주차 2일차: 웹 요소 찾기 실습 (reCAPTCHA 우회 버전)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def create_stealth_driver():
    """탐지 회피용 Chrome 드라이버 생성"""
    
    chrome_options = Options()
    
    # 자동화 탐지 우회 옵션들
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # 추가 탐지 우회 옵션들
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--disable-images")  # 이미지 로딩 안함 (속도 향상)
    
    # User-Agent 설정 (일반 사용자처럼 보이게)
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # WebDriver 속성 숨기기
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def element_finding_practice():
    """웹 요소 찾기 기초 실습 - reCAPTCHA 우회 버전"""
    
    print("=== 2일차 실습: 웹 요소 찾기 (탐지 우회) ===")
    
    # 탐지 우회 드라이버 생성
    driver = create_stealth_driver()

    try:
        driver.maximize_window()
        
        # 1. 구글 페이지로 이동 (천천히)
        print("1. 구글 페이지 접속...")
        driver.get("https://www.google.com")
        time.sleep(3)  # 더 긴 대기
        
        # 인간처럼 행동하기 위한 랜덤 대기
        print("   페이지 로딩 대기 중...")
        time.sleep(2)
        
        # 2. 검색창 찾기 - NAME으로 찾기 
        print("2. 검색창 찾기 (BY.NAME 사용)")
        try:
            search_box = driver.find_element(By.NAME, "q")
            print(f"   ✅ 검색창 찾음: {search_box.tag_name}")
        except Exception as e:
            print(f"   ❌ 검색창을 찾을 수 없음: {e}")
            print("   💡 수동으로 reCAPTCHA를 해결하세요 (30초 대기)")
            time.sleep(30)
            search_box = driver.find_element(By.NAME, "q")
        
        # 3. 검색어 입력 (천천히, 인간처럼)
        print("3. 검색어 입력: '파이썬 자동화' (천천히 타이핑)")
        search_box.clear()
        
        # 한 글자씩 천천히 입력 (인간처럼)
        search_text = "파이썬 자동화"
        for char in search_text:
            search_box.send_keys(char)
            time.sleep(0.1)  # 각 글자마다 0.1초 대기
        
        time.sleep(2)
        
        # 4. 엔터키로 검색 실행 
        print("4. 엔터키로 검색 실행")
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)  # 결과 로딩 충분히 대기
        
        # 5. 검색 결과 확인 
        print("5. 검색 결과 페이지 도달 확인")
        print(f"   현재 페이지 제목: {driver.title}")
        
        # reCAPTCHA가 나타났는지 확인
        if "unusual traffic" in driver.page_source.lower() or "robot" in driver.page_source.lower():
            print("   ⚠️  reCAPTCHA 감지됨! 수동으로 해결하세요.")
            print("   🤖 60초 동안 대기합니다...")
            time.sleep(60)
        
        print("\n✅ 2일차 기본 실습 완료!")
        
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        
    finally:
        print("\n브라우저를 10초 후 종료합니다...")
        time.sleep(10)
        driver.quit()

def alternative_search_practice():
    """대안: 다른 검색 엔진 사용"""
    
    print("\n=== 대안 실습: DuckDuckGo 사용 ===")
    
    driver = create_stealth_driver()
    
    try:
        driver.maximize_window()
        
        # DuckDuckGo 사용 (reCAPTCHA 없음)
        print("1. DuckDuckGo 페이지 접속...")
        driver.get("https://duckduckgo.com")
        time.sleep(3)
        
        # 검색창 찾기
        print("2. DuckDuckGo 검색창 찾기")
        search_box = driver.find_element(By.NAME, "q")
        print("   ✅ 검색창 찾기 성공!")
        
        # 검색어 입력
        print("3. 검색어 입력: 'Selenium Python'")
        search_box.send_keys("Selenium Python")
        time.sleep(2)
        
        # 검색 실행
        print("4. 검색 실행")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        
        print(f"   검색 완료! 페이지 제목: {driver.title}")
        print("   ✅ reCAPTCHA 없이 성공!")
        
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        
    finally:
        time.sleep(5)
        driver.quit()

def manual_captcha_practice():
    """수동 CAPTCHA 해결 연습"""
    
    print("\n=== 수동 reCAPTCHA 해결 연습 ===")
    print("💡 이 실습에서는 reCAPTCHA가 나타나면 직접 해결해보세요!")
    
    driver = create_stealth_driver()
    
    try:
        driver.maximize_window()
        
        print("1. 구글 접속...")
        driver.get("https://www.google.com")
        time.sleep(3)
        
        print("2. 검색창에 텍스트 입력...")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("브라우저 자동화 테스트")
        
        print("3. 검색 실행...")
        search_box.send_keys(Keys.RETURN)
        
        print("4. reCAPTCHA 확인 중...")
        time.sleep(5)
        
        # reCAPTCHA 감지 시 수동 해결 대기
        if "unusual traffic" in driver.page_source.lower():
            print("🤖 reCAPTCHA가 나타났습니다!")
            print("👆 직접 체크박스를 클릭하고 문제를 해결하세요.")
            print("⏰ 60초 동안 대기합니다...")
            time.sleep(60)
        
        print(f"✅ 최종 페이지: {driver.title}")
        
    except Exception as e:
        print(f"❌ 에러: {e}")
        
    finally:
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    print("🤖 reCAPTCHA 우회 실습을 시작합니다!")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    choice = input("\n실습 선택:\n1. 기본 실습 (탐지 우회)\n2. DuckDuckGo 대안\n3. 수동 해결 연습\n선택 (1-3): ")
    
    if choice == "1":
        element_finding_practice()
    elif choice == "2":
        alternative_search_practice()
    elif choice == "3":
        manual_captcha_practice()
    else:
        print("기본 실습을 실행합니다.")
        element_finding_practice()
    
    print("\n🎉 2일차 실습 완료!")
    print("📝 배운 내용: 요소 찾기 + reCAPTCHA 대응")