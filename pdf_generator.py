from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def create_payment_receipt(file_path, client_name, purchased_items, total_cost, receipt_id):
    page_width, page_height = A4
    pdf = canvas.Canvas(file_path, pagesize=A4)

    # Header
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(page_width / 2, page_height - 50, "Payment Receipt")

    # Receipt Details
    pdf.setFont("Helvetica", 12)
    pdf.drawString(30, page_height - 80, f"Receipt ID: {receipt_id}")
    pdf.drawString(30, page_height - 100, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    pdf.drawString(30, page_height - 120, f"Client Name: {client_name}")

    # Table Headers
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(30, page_height - 150, "Item Description")
    pdf.drawString(300, page_height - 150, "Qty")
    pdf.drawString(400, page_height - 150, "Price (Rs.)")

    # Line under headers
    pdf.line(30, page_height - 155, page_width - 30, page_height - 155)

    # List items
    current_y = page_height - 170
    pdf.setFont("Helvetica", 12)
    for description, quantity, unit_price in purchased_items:
        pdf.drawString(30, current_y, description)
        pdf.drawString(300, current_y, str(quantity))
        pdf.drawString(400, current_y, f"Rs. {unit_price:.2f}")
        current_y -= 20

    # Total cost
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(30, current_y - 20, f"Total Amount: Rs. {total_cost:.2f}")

    # Footer message
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawCentredString(page_width / 2, 30, "Thank you for your business!")

    pdf.save()

def input_purchased_items():
    products = []
    print("Please enter your purchased items (press Enter without input to finish):")
    while True:
        name = input("Item name: ").strip()
        if not name:
            break
        while True:
            try:
                qty = int(input("Quantity: "))
                if qty <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")
        while True:
            try:
                price = float(input("Price (Rs.): "))
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for price.")
        products.append((name, qty, price))
    return products

if __name__ == "__main__":
    customer = input("Enter the customer's full name: ").strip()
    receipt_num = input("Enter the receipt ID: ").strip()

    items = input_purchased_items()
    if not items:
        print("No items were added. Exiting program.")
    else:
        total_price = sum(q * p for _, q, p in items)
        create_payment_receipt("receipt.pdf", customer, items, total_price, receipt_num)
        print("Receipt has been generated successfully as 'receipt.pdf'.")
