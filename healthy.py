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
        print("売り切れです。　返金します。")
        sold_out = True
    else:
        sold_out = False

    return sold_out

#在庫ファイル読み込み
def read_stock():
    f = open("stock.txt", "r")
    list = []
    line = f.readline()
    list_name = []
    list_stock = []
    list_cal = []
    list_price = []

    while line:
        list.append(line)
        line = f.readline()
    f.close()

    for i in range(len(list)):
        hoge = list[i].rstrip('\n')
        item = hoge.split(",")
        list_name.append(item[0])
        list_stock.append(item[1])
        list_cal.append(item[2])
        list_price.append(int(item[3]))

    return list_name,list_stock,list_cal,list_price

#お金の支払い系
def flag(money,sales,item_price,num):

    items,stock,cal,price = read_stock()
    sold_out = soldout(stock[num])

    if money >= item_price and sold_out == False:
        print("商品を購入しますか？ Y/N")
        buy_flag = input().upper()
        if buy_flag == "Y":
            print("お買い上げありがとうございます。")
            money = money - item_price
            sales =  item_price + int(sales)
            print("お釣りは" + str(money) + "円です。")
            stock[num]=int(stock[num])-1
            f = open("stock.txt", "w")
            for i in range(len(items)):
                f.write(items[i] + "," +str(stock[i])+ "," + str(cal[i]) + "," + str(price[i]) + "\n")

            f.close()
        elif buy_flag == "N":
            print("お金を返却します。")
        else:
            print("YかNで答えてください！！！！！！")
            sales = flag(money,sales,item_price,num)

    elif money < item_price :
        while money < item_price :
            print("お金が" + str(item_price - money) + "円足りません。")
            while (1):
                try:
                    money_add = int(input("お金を入れてください>>>"))
                    break
                except:
                    print("お金以外を入れないでください")

            money=money+money_add
            print(str(money) + "円が入っています。")

        sales = flag(money, sales, item_price, num)
    return sales

#商品選択
def select_item(list_length):
    while(1):
        try:
            num = int(input("商品番号を入力してください>>>"))
            num-=1
            break
        except:
            print("番号を入力してください")
    if num > list_length or 0 > num :
        print('不正な入力です')
        num = select_item(list_length)

    return num

#main
def main_healthy():
    money = 0
    sales = read_sales()
    items, stock, cal,item_price = read_stock()
    print("-----------------------------------")
    for i in range(len(items)):
        if int(stock[i]) <= 0:
            print(str(i+1) + "   " + items[i] + " "+ cal[i] + "kcal" + " " + str(item_price[i]) + "円" + " (売り切れ) ")
        else:
            print(str(i+1) + "   " + items[i] + " "+cal[i] + "kcal" + " " + str(item_price[i]) + "円")

    print("-----------------------------------")
    num = select_item(len(stock))
    print("商品の値段は" + str(item_price[num]) + "円です")
    print("選んだ商品は" + items[num] + "です")
    print("-----------------------------------")

    #print(num)

    while(1):
        try:
            money = int(input("お金を入れてください>>>"))
            break
        except:
            print("お金以外を入れないでください")

    print(str(money)+"円が入っています。")

    sales = flag(money,sales,int(item_price[num]),num)
    write_sales(sales)
    #print("売り上げは"+str(sales))
    main_healthy()
if __name__ == "__main__":
    main_healthy()