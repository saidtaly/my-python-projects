quote = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

#replacing "!" with blank space
Quote = quote.replace("!"," ",8)
Quote=Quote.replace("!","")

#writing everything in upper letter
quote_upper= Quote.upper()
#writing the sentence in reverse
quote_reverse= Quote[42::-1]

#printing out the results
print(Quote)
print(quote_upper)
print(quote_reverse+".")