student_id = "67040463"

with open(f"{student_id}.txt", "r") as f:
    content = f.read()

digits = [int(ch) for ch in content if ch.isdigit()]

last_digit = int(student_id[-1])

if last_digit % 2 == 1:
    odd_digits = [d for d in digits if d % 2 == 1]
    total = sum(odd_digits)
    print(f"เลขตัวสุดท้ายของรหัสนิสิตเป็นเลขคี่ ({last_digit})")
    print(f"ผลรวมของตัวเลขเฉพาะเลขคี่ = {total}")
else:
    even_digits = [d for d in digits if d % 2 == 0]
    total = sum(even_digits)
    print(f"เลขตัวสุดท้ายของรหัสนิสิตเป็นเลขคู่ ({last_digit})")
    print(f"ผลรวมของตัวเลขเฉพาะเลขคู่ = {total}")
