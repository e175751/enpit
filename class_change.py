
class enPiT:

    def __init__(self,money,sales,item_price,sold_out):
        self.money = money
        self.sales = sales
        self.item_price = item_price
        self.sold_out = sold_out

    #売上を読み込む
    def read_sales(self):
        f = open("sales.txt", "r")
        sales = f.read()
        f.close()
        return sales

    #売上を書き込む
    def write_sales(self,sales):
        f = open("sales.txt", "w")
        f.write(str(sales))
        f.close()
        print("売り上げは"+str(sales))

    #在庫切れを売らないやつ
    def soldout(self,item):
        if (int(item) <= 0):
            print("売り切れです")
            return True
        else:
            return False

    #在庫ファイル読み込み
    def read_stock(self):
        f = open("stock.txt", "r")
        list=[]
        line = f.readline() 
        while line:
            list.append(line)
            line = f.readline()
        f.close()
        items_name=[]
        items_stock=[]
        for i in range(len(list)):
            hoge = list[i].rstrip('\n')
            item = hoge.split(",")
            items_name.append(item[0])
            items_stock.append(item[1])
       
        return items_name,items_stock

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

    def chase(self,money,item_price,buy_flag):
        pass

    #お金の支払い系
    def flag(self,money,sales,item_price):

        items_name,items_stock = self.read_stock()
        sold_out = self.soldout(int(items_stock[0]))
        """
        while money >= item_price and sold_out == False:
            print("商品を購入しますか？ Y/N")
            buy_flag = input().upper()
            if buy_flag == "Y":

            elif buy_flag == "N":
                print("お金を返却します。")
                break
        """
        if money >= item_price and sold_out == False:
            print("商品を購入しますか？ Y/N")
            buy_flag = input().upper()
            if buy_flag == "Y":
                print("お買い上げありがとうございます。")
                money = money - item_price
                sales = 100 + int(sales)
                print("お釣りは" + str(money) + "円です。")
                items_stock[0]=int(items_stock[0])-1
                f = open("stock.txt", "w")
                f.write(items_name[0] + "," +str(items_stock[0]))
                f.close()
            elif buy_flag == "N":
                print("お金を返却します。")
            else:
                print("YかNで答えてください！！！！！！")
                self.flag(money,sales,item_price)

        elif money < item_price :
            print("お金が" + str(item_price - money) + "円足りません。")
            
        self.write_sales(sales)

    #main
    def main_healthy(self):
        item_price = 100
        money=0
        sales = self.read_sales()
        print("商品の値段は"+str(item_price)+"円です")
        while(1):
            try:
                money = int(input("お金を入れてください>>>"))
                break
            except:
                print("お金以外を入れないでください")
        
        print(str(money)+"円が入っています。")

        self.flag(money,sales,item_price)

if __name__ == "__main__":
    money=0
    sales=0
    item_price=0
    sold_out=False
    enpit = enPiT(money,sales,item_price,sold_out)
    enpit.main_healthy()
