# within function main() we will convert dollars to whatever currencies come to mind

def main():
    user_input = input("Do you wish to convert US Dollars to another currency? (Yes/No): ")
    while user_input.lower() == "Yes".lower():
        print("This program converts US Dollars to whatever currency within the list")
        print("1: Pound Sterling (GBP)\n"
              "2: Euro (EUR)\n"
              "3: Japanese Yen (YPY)\n"
              "4: Australian Dollar (AUD)\n"
              "5: Canadian Dollar (CAD)\n"
              "6: Swiss Franc (CHF)\n"
              "7: Chinese Renminibi (CNH)\n"
              "8: Hong Kong Dollar (HKD)\n"
              "9: New Zealand Dollar (NZD) \n")

        dollars = eval(input("Enter the amount in dollars you wish to convert: "))
        option = input("Enter the currency you wish to convert US Dollars to: ")

        if option == "1":
            pounds = convert_to_pounds(dollars)
            print("That is", pounds, "pounds.\n")
        elif option == "2":
            euros = convert_to_euros(dollars)
            print("That is", euros, "euros.\n")
        elif option == "3":
            yen = convert_to_yen(dollars)
            print("That is", yen, "yen.\n")
        elif option == "4":
            ausd = convert_to_aus(dollars)
            print("That is", ausd, "australian dollars.\n")
        elif option == "5":
            cand = convert_to_can(dollars)
            print("That is", cand, "canadian dollars.\n")
        elif option == "6":
            swissf = convert_to_swiss(dollars)
            print("That is", swissf, "swiss francs.\n")
        elif option == "7":
            chinese_r = convert_to_chinese(dollars)
            print("That is", chinese_r, "chinese renminibi.\n")
        elif option == "8":
            hkd = convert_to_hong(dollars)
            print("That is", hkd, "hong kong dollars.\n")
        else:
            nzd = convert_to_nz(dollars)
            print("That is", nzd, "new zealand dollars.\n")

        user_input = input("Do you wish to still convert currency? (Yes/No): \n")


convert_to_pounds = lambda dollars: (dollars * 0.77).__round__()
convert_to_euros = lambda  dollars: (dollars * 0.91).__round__()
convert_to_yen = lambda dollars: (dollars * 140.34).__round__()
convert_to_aus = lambda dollars: (dollars * 1.50).__round__()
convert_to_can = lambda dollars: (dollars * 1.32).__round__()
convert_to_chinese = lambda dollars: (dollars * 7.21).__round__()
convert_to_hong = lambda dollars: (dollars * 7.83).__round__()
convert_to_swiss = lambda dollars: (dollars * 0.88).__round__()
convert_to_nz = lambda dollars: (dollars * 1.61).__round__()


main()