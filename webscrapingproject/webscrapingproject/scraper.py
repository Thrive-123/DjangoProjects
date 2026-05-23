from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

print("\nStudent Information")

student_info = soup.find_all('p')

for info in student_info[:3]:
    print(info.text)

print("\nUseful Links")

links = soup.find_all('a')

for link in links:
    print(link.text)

print("\nProgramming Skills")

skills = soup.find_all('li')

for skill in skills[:4]:
    print(skill.text)

print("\nProducts")

products = soup.find_all('div', class_='product')

for product in products:

    name = product.find('h3').text

    price = product.find('p').text

    print(name, "-", price)