materials_list = {
    # Hardware
    'hammer':['1 metal', '1 wood'],
    'tape':['1 metal', '1 plastic'],
    'shovel':['1 metal', '1 wood', '1 plastic'],
    'spatula':['2 metal', '2 plastic', '2 wood'],

    # Farmer's Market
    'veggies':['2 seed'],
    'flour':['2 seed', '2 cloth'],
    'melon':['2 seed', '1 plant'],

    # Furniture
    'chair':['2 wood', '1 nail', '1 hammer'],
    'table':['1 plank', '2 nail', '1 hammer'],

    # Building Supplies
    'nail':['2 metal'],
    'plank':['2 wood'],
    'brick':['2 rock'],
    'cement':['2 rock', '1 flask'],
    'glue':['1 plastic', '2 flask'],
}

# Print products available to manufacture
print("List of products: ")
print(", ".join(materials_list))

requested_products = input("Enter list of products: ")

# Loop through each product, and keep track of materials

materials_used = {}

for product_request in requested_products.split(', '):
    quantity = product_request.split(' ')[0]
    product = product_request.split(' ')[1]

    for i in range(1, int(quantity) + 1):
        for material_info in materials_list[product]:
            material_quantity = material_info.split(' ')[0]
            material = material_info.split(' ')[1]

            if material in materials_used:
                materials_used[material] = str(int(materials_used[material]) + int(material_quantity))
            else:
                materials_used[material] = material_quantity

# Output materials

print("MATERIALS:", end=" ")

i = 0

for material, material_quantity in materials_used.items():
    if i < len(materials_used) - 1:
        print(material_quantity + " " + material, end=", ")
    else:
        print(material_quantity + " " + material)

    i += 1