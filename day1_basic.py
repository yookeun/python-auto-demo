from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time;


# 첫 실행시 드라이버 다운로드 메시지가 나올 수 있다.

def basic_browser_cotrol():
    """ 기본 브라우저 제어 실습 """
    
    print("=== 1일차 실습: 기본 브라우저 제어")
    
    # chorm 옵션 설정
    chrome_options = Options()
    
    # Windows 11에서 Chrome 기본 경로
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    # 안정성을 위한 기본 옵션들 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # 1. chrome 드라이버 자동 설치 및 설정 
    print("1. Chrome 드라이버 설정 중...")
    #service = Service(ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()
    
    try:        
        # 2. 브라우저 창 크기 조절 
        print("2. 브라우저 창 크기 조절...")
        driver.maximize_window() # 최대화 
        
        print("3. 네이버 메인페이지 접속...")
        driver.get("https://www.naver.com")
        
        # 4. 페이지 정보 확인
        print(f"4. 현재 페이지 제목 : {driver.title}")
        print(f"   현재 URL : {driver.current_url}")
        
        # 5. 잠시 대기 (브라우저가 열린 상태를 확인하기 위해)
        print("5. 5초 대기중...(브라우저 확인)")
        time.sleep(5)
        
        # 6. 구글로 이동
        print("6. 구글로 이동...")
        driver.get("https://www.google.com")
        print(f"   새 페이지 제목: {driver.title}")
        
        # 7. 뒤로가기
        print("7. 뒤로가기...")
        driver.back()
        time.sleep(2)
        print(f"   뒤로간 후 제목: {driver.title} ")
        
        # 8. 앞으로가기
        print("8. 앞으로가기...")
        driver.forward()
        time.sleep(2)
        print(f"   앞으로간 후 제목: {driver.title} ")
        
        # 9. 페이지 새로고침
        print("9. 페이지 새로고침...")
        driver.refresh()
        time.sleep(2)
        
        print("✅ 모든 기본 동작 완료!")
        
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        
    finally:
        # 10. 브라우저 종료
        print("10. 브라우저 종료...")
        time.sleep(2)
        driver.quit()
        print("🎉 1일차 실습 완료!")
        
        
if __name__ == "__main__":
    basic_browser_cotrol()