#売上を読み込む
def read_sales():
    f = open("sales.txt", "r")
    sales = f.read()
    f.close()
    return sales

#売上を書き込む
def write_sales(sales):
    f = open("sales.txt", "w")
    f.write(str(sales))
    f.close()

#在庫切れを売らないやつ
def soldout(item):
    if (int(item) <= 0):
        print("売り切れです")
        sold_out = True
    else:
        sold_out = False

    return sold_out

#在庫ファイル読み込み
def read_stock():
    f = open("stock.txt", "r")
    items = f.readline().replace('\n', '').split(',')
    f.close()
    #print(items)
    return items


#お金の支払い系
def flag(money,sales,item_price):

    items = read_stock()
    print(items[0])
    sold_out = soldout(items[1])

    #item_count
    if money >= item_price and sold_out == False:
        print("商品を購入しますか？ Y/N")
        buy_flag = input().upper()
        if buy_flag == "Y":
            print("お買い上げありがとうございます。")
            money = money - item_price
            sales = 100 + int(sales)
            print("お釣りは" + str(money) + "円です。")
            items[1]=int(items[1])-1
            f = open("stock.txt", "w")
            f.write(items[0] + "," +str(items[1]))
            f.close()
        elif buy_flag == "N":
            print("お金を返却します。")
        else:
            print("YかNで答えてください！！！！！！")
            sales =flag(money,sales,item_price)

    elif money < item_price :
        print("お金が" + str(item_price - money) + "円足りません。")

    return sales

#main
def main_healthy():
    item_price = 100
    money=0
    sales = read_sales()
    print("商品の値段は"+str(item_price)+"円です")
    while(1):
        try:
            money = int(input("お金を入れてください>>>"))
            break
        except:
            print("お金以外を入れないでください")

    print(str(money)+"円が入っています。")

    sales = flag(money,sales,item_price)
    write_sales(sales)
    print("売り上げは"+str(sales))


if __name__ == "__main__":
    main_healthy()
