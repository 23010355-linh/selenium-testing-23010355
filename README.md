# Selenium Automation Testing

## Thông tin sinh viên

* Họ và tên: Lê Thị Hoài Linh
* MSSV: 23010355

## Mục tiêu

Tìm hiểu Selenium WebDriver và xây dựng các kịch bản kiểm thử tự động cho chức năng đăng nhập của website mẫu.

## Công nghệ sử dụng

* Python 3
* Selenium WebDriver
* Google Chrome
* ChromeDriver

## Website kiểm thử

https://the-internet.herokuapp.com/login

## Test Cases

### TC01 - Login Success

**Input**

* Username: tomsmith
* Password: SuperSecretPassword!

**Expected Result**

* Đăng nhập thành công.
* Chuyển đến trang Secure Area.

**Status:** PASS

---

### TC02 - Login Failed

**Input**

* Username: admin
* Password: 123456

**Expected Result**

* Hiển thị thông báo lỗi.
* Không đăng nhập được.

**Status:** PASS

---

### TC03 - Logout Success

**Steps**

* Đăng nhập thành công.
* Nhấn Logout.

**Expected Result**

* Quay lại màn hình Login.
* Hiển thị thông báo đăng xuất.

**Status:** PASS

## Cấu trúc thư mục

```text
selenium-testing/
├── test_login_success.py
├── test_login_fail.py
├── test_logout.py
└── README.md
```

## Kết quả

| Test Case | Result |
| --------- | ------ |
| TC01      | PASS   |
| TC02      | PASS   |
| TC03      | PASS   |

Tỷ lệ thành công: 100%.

## Kết luận

Đã xây dựng thành công 03 kịch bản kiểm thử tự động bằng Selenium WebDriver. Các chức năng đăng nhập hợp lệ, đăng nhập không hợp lệ và đăng xuất đều hoạt động đúng theo yêu cầu của hệ thống.
