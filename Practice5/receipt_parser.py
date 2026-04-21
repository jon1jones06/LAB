import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
        text = f.read()

def function(text):
    data = {
        "products": [],
        "total_price": 0.0,
        "date_time": "",
        "payment_method": "",
    }

    products = re.findall(r'(\d+)\.\n(.*?)\n([\d,]+)\s+x\s+([\d, ]+)\n([\d, ]+)', text, re.DOTALL)
    
    for prod in products:
        name = prod[1].replace('\n', ' ').strip()
        price = float(prod[2].replace(',', '.'))
        price_per_unit = float(prod[3].replace(' ', '').replace(',', '.'))
        total_price = float(prod[4].replace(' ', '').replace(',', '.'))
        
        data["products"].append({
            "name": name,
            "price": price,
            "price_per_unit": price_per_unit,
            "total_price": total_price
        })

    total = re.search(r'ИТОГО:\s+([\d\s,]+)', text)
    if total:
        data["total_price"] = float(total.group(1).replace(' ', '').replace(',', '.'))

    date_time = re.search(r'Время:\s+(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})', text)
    if date_time:
        data["date_time"] = date_time.group(1)

    if "Банковская карта" in text:
        data["payment_method"] = "Card"
    elif "Наличные" in text:
        data["payment_method"] = "Cash"

    return data

if text:
    parsed_result = function(text)
    print(json.dumps(parsed_result, indent=4))

#--------------------------------------------------------

n = (input()) 

def a1(text):
        return re.findall(r'ab*', text)

def a2(text):
        return re.findall(r'ab{2,3}', text)

def a3(text):
        return re.findall(r'[a-z]+_[a-z]+', text)
def a4(text):
        return re.findall(r'[A-Z][a-z]+', text)

def a5(text):
        return re.findall(r'a.*b$', text)

def a6(text):
        return re.sub(r'[ ,.]', ':', text)

def a7(text):
        return "".join(word.capitalize() for word in text.split('_'))

def a8(text):
        return re.findall(r'[A-Z][^A-Z]*', text)

def a9(text):
        return re.sub(r'(\w)([A-Z])', r'\1 \2', text)

def a10(text):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

print(a1(n), 1)
print(a2(n), 2)
print(a3(n), 3)
print(a4(n), 4)
print(a5(n), 5)
print(a6(n), 6)
print(a7(n), 7)
print(a8(n), 8)
print(a9(n), 9)
print(a10(n),10)