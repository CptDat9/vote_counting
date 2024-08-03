k = int(input("Nhập số người tham gia bầu chọn: "))
n = int(input("Nhập số lựa chọn: "))
votes = [0] * n
for i in range(k):
    print(f"Người thứ {i+1}, vui lòng nhập lựa chọn của bạn (1-{n}): ")
    choice = int(input()) - 1
    if 0 <= choice < n:
        votes[choice] += 1
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
        i -= 1  
results = [(i+1, votes[i]) for i in range(n)]
results.sort(key=lambda x: x[1], reverse=True)
print("Kết quả bầu chọn từ cao xuống thấp:")
for choice, vote in results:
    print(f"Lựa chọn {choice}: {vote} phiếu")

