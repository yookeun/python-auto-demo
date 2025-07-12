# 1주차 2일차: 웹 요소 찾기 실습 (수정 완료 버전)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def element_finding_practice():
    """웹 요소 찾기 기초 실습"""
    
    print("=== 2일차 실습: 웹 요소 찾기 ===")
    
    # 드라이버 실행 
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()
        
        # 1. 구글 페이지로 이동 
        print("1. 구글 페이지 접속...")
        driver.get("https://www.google.com")
        time.sleep(2)
        
        # 2. 검색창 찾기 - NAME으로 찾기 
        print("2. 검색창 찾기 (BY.NAME 사용)")
        search_box = driver.find_element(By.NAME, "q")
        print(f"   ✅ 검색창 찾음: {search_box.tag_name}")
        
        # 3. 검색어 입력 
        print("3. 검색어 입력: '파이썬 자동화'")
        search_box.clear()
        search_box.send_keys("파이썬 자동화")
        time.sleep(2)
        
        # 4. 엔터키로 검색 실행 
        print("4. 엔터키로 검색 실행")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # 5. 검색 결과 확인 
        print("5. 검색 결과 페이지 도달 확인")
        print(f"   현재 페이지 제목: {driver.title}")
        
        # 6. 다시 구글 홈으로 이동 
        print("\n6. 구글 홈으로 다시 이동...")
        driver.get("https://www.google.com")
        time.sleep(2)
        
        # 7. 검색 버튼 찾기 - NAME으로 찾기 (다른 방법)
        print("7. 검색창 다시 찾기")
        search_box2 = driver.find_element(By.NAME, "q")
        search_box2.send_keys("Selenium Python")
        time.sleep(1)
        
        # 8. 검색 버튼 클릭하기
        print("8. 검색 버튼 찾아서 클릭")
        try:
            # Google 검색 버튼 찾기 (여러 방법 시도)
            search_button = driver.find_element(By.NAME, "btnK")
            search_button.click()
            print("   ✅ 검색 버튼 클릭 성공")
        except Exception as e:            
            print("   ⚠️  검색 버튼을 찾을 수 없어서 엔터키 사용")
            search_box2.send_keys(Keys.RETURN)
            
        time.sleep(3)
        print(f"   검색 완료! 페이지 제목: {driver.title}")
                
        print("\n✅ 2일차 기본 실습 완료!")
        
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        
    finally:
        print("\n브라우저를 5초 후 종료합니다...")
        time.sleep(5)
        driver.quit()

def advanced_element_finding():
    """고급 요소 찾기 실습"""
    
    print("\n=== 2일차 고급 실습: 다양한 방법으로 요소 찾기 ===")
    
    driver = webdriver.Chrome()
    
    try:
        driver.maximize_window()
        
        # 네이버로 이동
        print("1. 네이버 페이지 접속...")
        driver.get("https://www.naver.com")
        time.sleep(3)
    
        # ID로 검색창 찾기
        print("2. 네이버 검색창 찾기 (BY.ID 사용)")
        try:
            naver_search = driver.find_element(By.ID, "query")
            print("   ✅ ID로 검색창 찾기 성공")
            
            # 검색어 입력 
            naver_search.clear()
            naver_search.send_keys("브라우저 자동화")
            time.sleep(2)
            
            # CLASS_NAME으로 검색 버튼 찾기 
            print("3. 검색 버튼 찾기 (BY.CLASS_NAME 시도)")
            try:
                search_btn = driver.find_element(By.CLASS_NAME, "btn_search")
                search_btn.click()
                print("   ✅ 클래스명으로 검색 버튼 클릭 성공")
            except:
                print("   ⚠️  클래스명으로 안되어서 엔터키 사용")
                naver_search.send_keys(Keys.RETURN)
            time.sleep(3)
            
        except Exception as e:
            print(f"   ❌ 네이버 검색창을 찾을 수 없음: {e}")
            
        # TAG_NAME으로 링크들 찾기
        print("\n4. 페이지의 모든 링크 찾기 (BY.TAG_NAME)")
        links = driver.find_elements(By.TAG_NAME, "a")  # 오타 수정: linkes → links
        print(f"   페이지에서 찾은 링크 개수: {len(links)}개")
        
        # 처음 5개 링크의 텍스트 출력 
        print("   처음 5개 링크:")
        for i, link in enumerate(links[:5]):  # 오타 수정: linke → link
            link_text = link.text.strip()
            if link_text:  # 텍스트가 있는 링크만
                print(f"   {i+1}. {link_text[:30]}...")  # ... 추가
                
        print("\n✅ 고급 실습 완료!")
        
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        
    finally:
        print("\n브라우저를 5초 후 종료합니다...")
        time.sleep(5)
        driver.quit()

def practice_different_methods():
    """다양한 찾기 방법 연습"""    
    
    print("\n=== 요소 찾기 방법 정리 ===")
    print("🔍 Selenium에서 요소를 찾는 8가지 방법:")
    print("1. By.ID           - 고유 ID로 찾기 (가장 빠름)")
    print("2. By.NAME         - name 속성으로 찾기")
    print("3. By.CLASS_NAME   - 클래스명으로 찾기")
    print("4. By.TAG_NAME     - HTML 태그로 찾기")
    print("5. By.LINK_TEXT    - 링크 텍스트로 찾기")
    print("6. By.PARTIAL_LINK_TEXT - 부분 링크 텍스트로 찾기")
    print("7. By.XPATH        - XPath로 찾기 (강력하지만 복잡)")
    print("8. By.CSS_SELECTOR - CSS 선택자로 찾기")
    print("\n오늘은 1,2,3,4번을 배웠습니다!")
    print("내일은 5,6번을, 모레는 7,8번을 배울 예정입니다.")

if __name__ == "__main__":
    # 기본 실습
    element_finding_practice()
    
    # 고급 실습 진행 여부 확인 (사용자 선택 기능 복원)
    print("\n" + "="*50)
    user_choice = input("고급 실습도 진행하시겠습니까? (y/n): ")
    
    if user_choice.lower() == 'y':
        advanced_element_finding()
    
    # 방법 정리
    practice_different_methods()
    
    print("\n🎉 2일차 실습 완료! 구글시트에 체크하세요!")