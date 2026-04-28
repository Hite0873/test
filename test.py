import random

# 1. 컴퓨터가 1에서 100 사이의 랜덤 숫자를 선택합니다.
secret_number = random.randint(1, 100)
attempts = 0

print("🤖: 1부터 100 사이의 숫자 하나를 골랐어. 맞춰봐!")

# 2. 맞힐 때까지 무한 반복!
while True:
    try:
        # 사용자로부터 입력을 받습니다.
        guess = int(input("숫자를 입력하세요: "))
        attempts += 1

        # 3. 비교 및 힌트 제공
        if guess < secret_number:
            print("📈 UP! 더 큰 숫자를 불러봐.")
        elif guess > secret_number:
            print("📉 DOWN! 더 작은 숫자를 불러봐.")
        else:
            print(f"🎉 정답이야! {attempts}번 만에 맞췄네!")
            break  # 정답을 맞히면 반복문을 종료합니다.
            
    except ValueError:
        print("💡 숫자만 입력해줘!")
