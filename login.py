users = 
{
    "user1": "password1",
    "user2": "password2",
}

def login(username, password):
    if username in users and users[username] == password:
        print("로그인 성공")
        return True
    else:
        print("로그인 실패! 다시 시도하세요.")
        return False

if __name__ == "__main__":
    user = input("사용자 이름을 입력하세요: ")
    pwd = input("비밀번호를 입력하세요: ")
    login(user, pwd)

