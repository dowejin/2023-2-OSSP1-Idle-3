import bcrypt

# 사용자 데이터: 비밀번호는 해시로 저장
users = {
    "user1": bcrypt.hashpw("password1".encode(), bcrypt.gensalt()),
    "user2": bcrypt.hashpw("password2".encode(), bcrypt.gensalt()),
}

# 로그인 상태를 추적하는 변수
is_logged_in = False

def login(username, password):
    """로그인 함수: 사용자가 입력한 아이디와 비밀번호를 확인합니다."""
    global is_logged_in
    if username in users:
        if bcrypt.checkpw(password.encode(), users[username]):
            print("로그인 성공")
            is_logged_in = True
            return True
    print("로그인 실패! 다시 시도하세요.")
    return False

def logout():
    """로그아웃 함수: 사용자의 로그인 상태를 종료합니다."""
    global is_logged_in
    if is_logged_in:
        is_logged_in = False
        print("로그아웃 성공")
        return True
    else:
        print("로그인 상태가 아닙니다.")
        return False

def signup(username, password):
    """회원가입 함수: 새로운 사용자를 생성하고 비밀번호를 해시하여 저장합니다."""
    if username in users:
        print("이미 존재하는 사용자 이름입니다. 다른 이름을 사용하세요.")
        return False
    # 비밀번호 해시화 후 저장
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed_password
    print("회원가입 성공! 이제 로그인하세요.")
    return True

if __name__ == "__main__":
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 로그인")
        print("2. 로그아웃")
        print("3. 회원가입")
        print("4. 종료")
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
            new_user = input("새로운 사용자 이름을 입력하세요: ")
            new_pwd = input("새로운 비밀번호를 입력하세요: ")
            signup(new_user, new_pwd)

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("올바른 선택이 아닙니다. 다시 시도하세요.")

