# 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # %d 는 항상 정수값만 넣을 수 있음.
print("나는 %s을 좋아해요." % "파이썬") # %s 는 문자열, 정수 전부 출력 가능함
print("Apple 은 %c로 시작해요." % "A") # %c 는 한글자만 받음

print("나는 %s살입니다." % 20) # %d 는 항상 정수값만 넣을 수 있음.
print("나는 %s색과 %s색을 좋아해요." % ("파란", " 빨간"))

# 방법 2
print("나는 {}살입니다.".format(20)) # 중괄호에 20 기입
print("나는 {}색과 {}색을 좋아해요." .format("파란", " 빨간"))
# 숫자를 넣으면 원하는 위치의 단어를 넣을 수 있음
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", " 빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", " 빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {color}살이며, {age}색을 좋아해요.".format(age = 20, color = "빨간"))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
# f 를 사용하면 실제 변수에 저장된 값을 가져올수있음