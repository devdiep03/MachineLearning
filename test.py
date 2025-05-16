import pickle

file_path = r'C:\Users\hongd\Documents\Zalo Received Files\ML\diabetes.pkl'
try:
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    print("Mô hình đã được tải thành công:", type(model))
except Exception as e:
    print("Lỗi khi tải mô hình:", e)
