from utils import calculate_discount

def main():
    final_price = calculate_discount(1000, 20)
    print(f"Итоговая цена со скидкой 20%: {final_price} руб.")

if __name__ == "__main__":
    main()