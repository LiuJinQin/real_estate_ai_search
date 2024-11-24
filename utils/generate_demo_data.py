import sqlite3
import random
import datetime

# 连接数据库
conn = sqlite3.connect('real_estate.db')
cursor = conn.cursor()

# 创建 properties 表
cursor.execute('''
CREATE TABLE IF NOT EXISTS properties (
    property_id INTEGER PRIMARY KEY,
    category TEXT,
    price REAL,
    property_type TEXT,
    building_style TEXT,
    bedrooms INTEGER,
    bathrooms INTEGER,
    parking_spaces INTEGER,
    pricing_method TEXT,
    listing_date DATE,
    square_feet INTEGER,
    land_area INTEGER,
    construction_year INTEGER,
    ownership_type TEXT,
    government_valuation REAL,
    suburb TEXT,
    district TEXT,
    region TEXT,
    open_date DATE,
    zoning TEXT
)
''')

# 创建 schools 表
cursor.execute('''
CREATE TABLE IF NOT EXISTS schools (
    suburb TEXT,
    district TEXT,
    region TEXT,
    name TEXT,
    decile INTEGER
)
''')

# 示例数据选项
suburbs = ["Remuera", "Epsom", "Mt Eden", "Ponsonby", "Parnell"]
districts = ["Auckland Council", "Wellington City Council", "Christchurch City Council"]
regions = ["Auckland Region", "Wellington Region", "Canterbury Region"]
property_types = ["独立屋", "公寓", "单元房", "城市屋", "排房", "自住投资", "乡村别墅", "乡村住宅建地", "建地"]
building_styles = ["当代风格", "豪华现代风", "传统风格", "乡村风", "海滩热带风", "维多利亚地中海"]
pricing_methods = ["要价", "价格可议", "拍卖", "投标", "POA", "出价", "限期出售", "其他"]
ownership_types = ["全幅地永久产权", "半幅地永久产权", "租赁产权", "公寓/单元房", "分时度假物业",
                   "Supplementary record sheet", "Records embodied in the register", "Gazette notice", "Life estate"]
zoning_types = ["Single house zone", "Mixed housing suburban zone", "Mixed housing Urban zone",
                "Terrace and apartment zone", "Rural and coastal zone", "Large lot zone", "Other zones"]

# 插入示例数据到 properties 表
for i in range(100):
    category = random.choice(["买房", "全新房", "最近成交", "估价", "房产开发", "租房"])
    price = random.randint(100000, 10000000)  # 房产价格在 $100,000 到 $10,000,000 之间
    property_type = random.choice(property_types)
    building_style = random.choice(building_styles)
    bedrooms = random.randint(1, 5)
    bathrooms = random.randint(1, 5)
    parking_spaces = random.randint(1, 5)
    pricing_method = random.choice(pricing_methods)
    listing_date = datetime.date.today() - datetime.timedelta(days=random.randint(1, 365))  # 随机日期
    square_feet = random.randint(50, 500)
    land_area = random.randint(100, 1000)
    construction_year = random.randint(1900, 2023)
    ownership_type = random.choice(ownership_types)
    government_valuation = random.uniform(50, 500)  # 政府估价（万元）
    suburb = random.choice(suburbs)
    district = random.choice(districts)
    region = random.choice(regions)
    open_date = datetime.date.today() - datetime.timedelta(days=random.randint(1, 365))
    zoning = random.choice(zoning_types)

    cursor.execute('''
        INSERT INTO properties (
            property_id, category, price, property_type, building_style, bedrooms,
            bathrooms, parking_spaces, pricing_method, listing_date, square_feet,
            land_area, construction_year, ownership_type, government_valuation, 
            suburb, district, region, open_date, zoning
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        i + 1, category, price, property_type, building_style, bedrooms, bathrooms,
        parking_spaces, pricing_method, listing_date, square_feet, land_area,
        construction_year, ownership_type, government_valuation, suburb, district,
        region, open_date, zoning
    ))

# 插入示例数据到 schools 表
for _ in range(100):
    suburb = random.choice(suburbs)
    district = random.choice(districts)
    region = random.choice(regions)
    name = f"{random.choice(['Central', 'West', 'East', 'North', 'South'])} {random.choice(['Primary', 'College', 'Grammar', 'High', 'Intermediate'])} School"
    decile = random.randint(1, 10)

    cursor.execute("INSERT INTO schools (suburb, district, region, name, decile) VALUES (?, ?, ?, ?, ?)",
                   (suburb, district, region, name, decile))

# 提交更改并关闭连接
conn.commit()
conn.close()

print("Demo data for 'properties' and 'schools' tables has been successfully inserted into the database.")
