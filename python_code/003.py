html = """

<!DOCTYPE html>
<html>
<head>
	<title>Basic Web Scraping</title>
</head>
<body>

	<h2 style="text-align: center">BASIC BLOG PAGE</h2>


	<div class="post">
		<h1>Post Heading 1</h1>
		<p>1 This is post content . lorem Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
		proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
	</div>

	<div class="post">
		<h1>Post Heading 2</h1>
		<p>2 This is post content . lorem Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
		proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
	</div>


	<img src="img/wordpress.png">
	<p class="name">Wordpress</p>
	<p id="status">PHP base CMS</p>

	<table>
		<tr>
			<td>ID</td>
			<td>Name</td>
			<td>Salary</td>
		</tr>
		<tr>
			<td>01</td>
			<td>Md Mortuza Hossain</td>
			<td>40000</td>
		</tr>
		<tr>
			<td>02</td>
			<td>Zakariya</td>
			<td>40000</td>
		</tr>
		<tr>
			<td>03</td>
			<td>Hasan</td>
			<td>30000</td>
		</tr>
	</table>



</body>
</html>
"""


from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
title = soup.find('title')

pageheading = soup.find('h2')

post1title = soup.find('h1')
allh1 = soup.find_all('h1')

# print title.text
# print pageheading.text
