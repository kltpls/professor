

def main():
    dan = 5
    print("구구단을 출력합니다.")
    with open("gugudan.html", "w") as f:
        f.write("<html>\n")
        for j in range(1, 10):
            f.write(f"{dan} X {j} = <strong>{dan*j}</strong><br>\n")
        f.write("</html>\n")

if __name__ == "__main__":
    main()