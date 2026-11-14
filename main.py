import random

# Store 10 different quotes as a list of tuples (quote, author) 
quotes = [
    ("The only way to achieve the impossible is to believe it is possible.", "Charles Kingsleigh"),
    ("In the middle of difficulty lies opportunity.", "Albert Einstein"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("The only thing we have to fear is fear itself.", "Franklin D. Roosevelt"),
    ("Life is what happens when you're busy making other plans.", "John Lennon"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
    ("It is during our darkest moments that we must focus to see the light.", "Aristotle"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("The best way to predict the future is to create it.", "Peter Drucker")
]

# Use import random to display a random quote each time it runs
random_quote = random.choice(quotes) 

# Output format (e.g., "Quote here. - Author") 
print(f"\n{random_quote[0]} - {random_quote[1]}\n")

