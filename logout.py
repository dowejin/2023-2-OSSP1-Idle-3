import bcrypt

# 사용자 데이터: 비밀번호는 해시로 저장
users = {
    "user1": bcrypt.hashpw("password1".encode(), bcrypt.gensalt()),
    "user2": bcrypt.hashpw("password2".encode(), bcrypt.gensalt()),
}

# 로그인 상태를 추적하는 변수
is_logged_in = False

def login(username, password):
    global is_logged_in
    # 사용자가 있는지 확인
    if username in users:
        # 비밀번호 확인
        if bcrypt.checkpw(password.encode(), users[username]):
            print("로그인 성공")
            is_logged_in = True
            return True
    print("로그인 실패! 다시 시도하세요.")
    return False

def logout():
    global is_logged_in
    if is_logged_in:
        is_logged_in = False
        print("로그아웃 성공")
        return True
    else:
        print("로그인 상태가 아닙니다.")
        return False

if __name__ == "__main__":
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 로그인")
        print("2. 로그아웃")
        print("3. 종료")
        choice = input("선택: ")

        if choice == "1":
            if is_logged_in:
                print("이미 로그인 상태입니다.")
            else:
                user = input("사용자 이름을 입력하세요: ")
                pwd = input("비밀번호를 입력하세요: ")
                login(user, pwd)
        elif choice == "2":
            logout()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 시도하세요.")

