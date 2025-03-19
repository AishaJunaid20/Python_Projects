
    books = load_books()
    
    if not books:
        st.warning("📚 No books found in the library.")
        return
    
    table = [[i+1, book["Title"], book["Author"], book["Genre"], book["Year"], book["Status"]] for i, book in enumerate(books)]
    st.text("📖 Your Personal Library:")
    st.text(tabulate(table, headers=["ID", "Title", "Author", "Genre", "Year", "Status"], tablefmt="grid"))

# Add a new book
def add_book(title, author, genre, year, status):
    books = load_books()
    books.append({"Title": title, "Author": author, "Genre": genre, "Year": year, "Status": status})
    save_books(books)

# Update book status
def update_book_status(book_id, new_status):
    books = load_books()
    if 0 < book_id <= len(books):
        books[book_id - 1]["Status"] = new_status
        save_books(books)
        st.success("✅ Book status updated successfully!")
    else:
        st.error("⚠ Invalid Book ID!")

# Delete a book
def delete_book(book_id):
    books = load_books()
    if 0 < book_id <= len(books):
        removed_book = books.pop(book_id - 1)
        save_books(books)
        st.success(f"❌ '{removed_book['Title']}' has been deleted.")
    else:
        st.error("⚠ Invalid Book ID!")

# Streamlit UI
st.title("📚 Personal Library Manager")

# Add new book form
with st.form("add_book_form"):
    st.subheader("➕ Add a New Book")
    title = st.text_input("📌 Book Title")
    author = st.text_input("✍ Author")
    genre = st.text_input("📚 Genre")
    year = st.text_input("📅 Year")
    status = st.selectbox("🔖 Reading Status", ["Not Started", "In Progress", "Completed"])
    submit_button = st.form_submit_button("Add Book")

    if submit_button and title and author and genre and year:
        add_book(title, author, genre, year, status)
        st.success(f"✅ '{title}' has been added to your library!")

# Display books
st.subheader("📖 Library Collection")
display_books()

# Update book status
st.subheader("📝 Update Book Status")
book_id = st.number_input("📌 Enter Book ID to Update", min_value=1, step=1)
new_status = st.selectbox("🔖 New Status", ["Not Started", "In Progress", "Completed"])
if st.button("Update Status"):
    update_book_status(book_id, new_status)

# Delete a book
st.subheader("❌ Delete a Book")
delete_id = st.number_input("📌 Enter Book ID to Delete", min_value=1, step=1)
if st.button("Delete Book"):
    delete_book(delete_id)
