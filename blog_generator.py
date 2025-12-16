def generate_blog(product, keywords):
    keyword_str = ", ".join(keywords)

    blog = f"""
<h2>{product['title']} Review – Is It Worth Buying?</h2>

<p>The <b>{product['title']}</b> is currently trending among online shoppers.
Priced at {product['price']}, this product has gained popularity due to its
quality and affordability.</p>

<p>When looking for the best options related to <b>{keyword_str}</b>,
this product stands out for its performance and customer satisfaction.</p>

<p>One of the main reasons people are searching for <b>{keywords[0]}</b>
is its long-lasting value and ease of use.</p>

<p>Overall, if you are planning to buy a reliable product related to
<b>{keyword_str}</b>, this is a smart choice in 2025.</p>
"""
    return blog
