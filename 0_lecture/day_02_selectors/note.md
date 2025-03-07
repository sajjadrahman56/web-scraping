## Day 02 [ Note ]

### Understanding Locators in Selenium Web Automation

Selenium is a popular tool for automating web applications. It allows you to interact with web pages, just like a human would. To do this, Selenium uses **locators** to find elements on a webpage. Let’s break down different types of locators with simple code examples.

---

### 1. **Using the ID Locator**

The **ID locator** is one of the most reliable ways to find elements because each ID should be unique on the page. In this example, we will search for "T-shirt" on a website using the search bar.

#### HTML Code:
```html
<input type="text" id="search_query_top" name="search_query" placeholder="Search">
```

#### Selenium Code:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open the Chrome browser
driver = webdriver.Chrome()

# Go to the website
driver.get("http://automationpractice.com/index.php")

# Find the search bar by its ID and type 'T-shirt'
driver.find_element(By.ID, "search_query_top").send_keys("T-shirt")
```

Here, we locate the search bar using its ID (`search_query_top`) and input the search term "T-shirt."

---

### 2. **Using the Name Locator**

Another way to locate elements is by using the **NAME locator**, which is especially useful for form inputs like buttons.

#### HTML Code:
```html
<button type="submit" name="submit_search" class="btn btn-default button-search">
  Search
</button>
```

#### Selenium Code:
```python
# Find the submit button by its name and click it
driver.find_element(By.NAME, "submit_search").click()
```

In this example, we find the search button by its **name** (`submit_search`) and click it.

---

### 3. **Using Link Text and Partial Link Text**

If you want to click on links, you can use **Link Text** or **Partial Link Text** locators. These are helpful when the link's text is unique.

#### HTML Code:
```html
<a href="http://automationpractice.com/index.php?id_product=7" title="Printed Chiffon Dress">
  Printed Chiffon Dress
</a>
```

#### Selenium Code:
```python
# Find the link by full text and click it
driver.find_element(By.LINK_TEXT, "Printed Chiffon Dress").click()

# Alternatively, find the link using partial text and click it
driver.find_element(By.PARTIAL_LINK_TEXT, "Chiffon Dress").click()
```

We locate the link using either the full text (**LinkText**) or a part of it (**PartialLinkText**).

---

### 4. **Using Class Name Locator**

The **Class Name** locator is useful when you want to find multiple elements with the same class, like images in a gallery or items in a list.

#### HTML Code:
```html
<ul class="homeslider">
  <li class="homeslider-container">
    <img src="image1.jpg" alt="Image 1">
  </li>
</ul>
```

#### Selenium Code:
```python
# Find all elements with the class 'homeslider-container'
sliders = driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(sliders))  # Prints the number of items with this class
```

Here, we use **find_elements** to return a list of elements with the class name `homeslider-container`.

---

### 5. **Using Tag Name Locator**

The **Tag Name** locator helps when you need to interact with elements based on their HTML tag, such as links or divs.

#### HTML Code:
```html
<a href="http://example.com">Click Here</a>
```

#### Selenium Code:
```python
# Find all 'a' tags (links) and print how many there are
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
```

This code will find all anchor (`<a>`) tags on the page and count them.

---

### 6. **CSS Selectors**

CSS selectors provide a flexible way to find elements based on their tag, class, or attributes. You can combine these to make precise selectors.

#### CSS Selectors Examples:
- Tag and ID: `input#email`
- Tag and Class: `input.inputtext`
- Tag and Attribute: `input[data-testid="royal_email"]`
- Tag, Class, and Attribute: `input.inputtext[data-testid="royal_email"]`

#### Selenium Code:
```python
# Using a CSS selector to find an element by class and attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid='royal_email']").send_keys("abc@gmail.com")
```

In this example, we locate the email input field using a CSS selector that combines the **tag**, **class**, and **attribute**.

---

### 7. **XPath (Custom Locators)**

XPath allows you to navigate through elements in an XML-like structure, and it’s often used when other locators aren’t sufficient.

#### XPath Example:
```xpath
//input[@id='email']
```

#### Selenium Code:
```python
# Find an element using XPath
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("abc@gmail.com")
```

This is a very powerful tool when other locators fail.

---

### Conclusion

Understanding locators in Selenium is essential for web automation. By using different types of locators like **ID**, **Name**, **Class Name**, **Tag Name**, **CSS Selector**, and **XPath**, you can efficiently interact with various web elements. The examples provided here are beginner-friendly and aim to help you get started with Selenium for web automation.
