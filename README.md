<h1>Goodreads Book Data Analysis</h1>

<h2>Project Development Journal</h2>

<h3><code style="color:blue">Problem Statement</code></h3>
<strong><a href=""></a></strong>

<h3><code style="color:blue">Data Collection</code></h3>
<strong></strong>

<!-- <h3><code style="color:blue"><a href="https://public.tableau.com/app/profile/neloy.barman/viz/GoodreadsBookDataAnalysis/author__book_data">Analysis</a> Requirements Blueprint</code></h3> -->

* <strong>Find the average ratings for each author based on the book data.(Top 5)</strong>
* <strong>Find the number of books written by an author.(Top 5)</strong> 
* <strong>Find out the top 5 most rated books.</strong>
* <strong>Find out the top 5 books with most number of ratings.</strong>
* <strong>Find out the top 5 books with most number of reviews.</strong>
* <strong>Plot a relationship between the total no. of reviews and avg ratings as well as total no. of ratings.</strong>
* <strong>Do the total number of 5 star, 4 star and 2 star ratings create an impact to get the book a descent avg. ratings? Do they have any graphical relationship?</strong>
* <strong>In which number of genres, the avg. ratings and no. of reviews are mostly populated?</strong>
* <strong>Find if there exists any relationship between descriptions word count and avg. ratings and no. of reviews.</strong>



<h3><code style="color:blue">DashBoard</code></h3>
<!-- <strong>You can find all the analysis within this <a href="https://public.tableau.com/app/profile/neloy.barman/viz/GoodreadsBookDataAnalysis/author__book_data">Tableau DashBoard</a></strong> -->

<h3><code style="color:blue">Analysis and Observations</code></h3>

<h4>i. Author and Book Data Analysis</h4>
<img src="readmeFileImages/dashboard_1.png">

<ul>
    <li>
        <strong>Author Data Findings</strong>
        <ul>
            <li>
                <strong>Top 5 authors with most avg. ratings based on book ratings: -</strong>
                    <table align="center">
                        <tr align="center">
                            <th>Author</th>
                            <th>Avg. Ratings</th>
                        </tr>
                        <tr align="center">
                            <td>Mustafa Kemal Atatürk</td>
                            <td>4.81</td>
                        </tr>
                        <tr align="center">
                            <td>Quino</td>
                            <td>4.77</td>
                        </tr>
                        <tr align="center">
                            <td>MsKingBean89</td>
                            <td>4.753</td>
                        </tr>
                        <tr align="center">
                            <td>Hayao Miyazaki</td>
                            <td>4.75</td>
                        </tr>
                        <tr align="center">
                            <td>Chanel Miller</td>
                            <td>4.71</td>
                        </tr>
                    </table>
            </li>
            <li>
                <strong>Top 5 authors with most no. of books and avg. ratings: -</strong>
                <table align="center">
                    <tr align="center">
                        <th>Author</th>
                        <th>No. of Books</th>
                        <th>Avg. Ratings</th>
                    </tr>
                    <tr align="center">
                        <td>Stephen King</td>
                        <td>82</td>
                        <td>4.022</td>
                    </tr>
                     <tr align="center">
                        <td>Agatha Christie</td>
                        <td>77</td>
                        <td>3.902</td>
                    </tr>
                     <tr align="center">
                        <td>Sherrilyn Kenyon</td>
                        <td>73</td>
                        <td>4.236</td>
                    </tr>
                     <tr align="center">
                        <td>James Patterson</td>
                        <td>69</td>
                        <td>3.956</td>
                    </tr>
                     <tr align="center">
                        <td>Misba</td>
                        <td>57</td>
                        <td>4.595</td>
                    </tr>
                </table>
            </li>
        </ul>
    </li>
    <li>
        <strong>Book Data Findings</strong>
        <ul>
            <li>
                <strong>Top 5 most rated books: -</strong>
                <table align="center">
                    <tr align="center">
                        <th>Title</th>
                        <th>Avg. Ratings</th>
                    </tr>
                    <tr align="center">
                        <td>A Song to Drown Rivers</td>
                        <td>4.92</td>
                    </tr>
                    <tr align="center">
                        <td>Nutuk</td>
                        <td>4.81</td>
                    </tr>
                    <tr align="center">
                        <td>All the Young Dudes - Volume Two: Years 5 - 7</td>
                        <td>4.81</td>
                    </tr>
                    <tr align="center">
                        <td>The Complete Calvin and Hobbes</td>
                        <td>4.80</td>
                    </tr>
                    <tr align="center">
                        <td>Mark of the Lion Trilogy</td>
                        <td>4.78</td>
                    </tr>
                </table>
            </li>
            <li>
                <strong>Top 5 books with most number of ratings: -</strong>
                <table align="center">
                    <tr align="center">
                        <th>Title</th>
                        <th>No. of Ratings</th>
                    </tr>
                    <tr align="center">
                        <td>Harry Potter and the Sorcerer’s Stone</td>
                        <td>9,699,750</td>
                    </tr>
                    <tr align="center">
                        <td>Harry Potter and the Philosopher’s Stone</td>
                        <td>9,679,526</td>
                    </tr>
                    <tr align="center">
                        <td>Hungerspelen</td>
                        <td>8,325,671</td>
                    </tr>
                    <tr align="center">
                        <td>The Hunger Games</td>
                        <td>8,324,081</td>
                    </tr>
                    <tr align="center">
                        <td>To Kill a Mockingbird</td>
                        <td>5,917,556</td>
                    </tr>
                </table>
            </li>
            <li>
                <strong>Top 5 books with most number of reviews: -</strong>
                <table align="center">
                    <tr align="center">
                        <th>Title</th>
                        <th>No. of Reviews</th>
                    </tr>
                    <tr align="center">
                        <td>Los siete maridos de Evelyn Hugo</td>
                        <td>248,179</td>
                    </tr>
                    <tr align="center">
                        <td>The Seven Husbands of Evelyn Hugo</td>
                        <td>247,810</td>
                    </tr>
                    <tr align="center">
                        <td>It Ends with Us</td>
                        <td>234,402</td>
                    </tr>
                    <tr align="center">
                        <td>Verity</td>
                        <td>216,065</td>
                    </tr>
                    <tr align="center">
                        <td>Hungerspelen</td>
                        <td>210,444</td>
                    </tr>
                </table>
            </li>
        </ul>
    </li>
</ul>

<h4>ii. Different Kinds of Relationships Findings</h4>
<img src="readmeFileImages/dashboard_2.png">
<ul>
    <li>
        <strong>Reviews vs Avg. Ratings and Total No. of Ratings</strong></br>
        <strong>I plotted a relationship between the total number of reviews for a book with it's average ratings and total number of ratings given by the readers. The main goal here was to find out if any kind of dependency on each other exists that may result in increasing or decreasing values. In the case of reviews vs avg. ratings, the most avg. rated book "A Song to Drown River" with 4.92 value has only 46 reviews whereas the lowest one "Revealing Eden" with 2.00 value has 375 reviews. The book with most number of reviews is "Los siete maridos de Evelyn Hugo" and it's average ratings is 4.43. Proceeding to reviews vs no. of ratings plot, we could have expected a relationship but the values got scattered. Here the book with most number of ratings is "Harry Potter and the Sorcerer's Stone" with a value of 9699750 has 156453 reviews. The lowest one here has 9 ratings and 1 reviews. So, there is no dependent relationship between any of these variables.</strong>
    </li>
    <li>
        <strong>Descriptions Word vs Avg. Ratings and No. of Reviews</strong></br>
        <strong>Different descriptions have different word counts. So, I plotted the words count and wanted to see if any dependency occurs with avg. ratings and total reviews. Looking at average ratings, some points may show relation. But the overall situation shows nothing. In the case of plot with total reviews, the book with 1201 descriptive words has only 358 reviews whereas the one with 199 words got 248179 reviews. The lowest word count I got is only 1. So, there is no relationship in between those both practical and hypothetical variables.</strong>
    </li>
    <li>
        <strong>Genre Count vs Avg. Ratings and No. of Reviews</strong></br>
        <strong>In the website, a book falls within multiple genres. So, I tried to figure out in which area, the average ratings and reviews mostly depend. In the case of average ratings, the darker regions are mostly closer to 4.00 value. Looking at Y-axis, the books that are categorized between 12 and 14 closer values, fall within the darker areas. Going to the number of reivews case, in the same way 12-14 closer values categoried books get a descent amount of reviews. So, we can conclude saying people are interested in books that contains writings relatable to 12-14 genres. </strong>
    </li>
    <li>
        <strong>Avg. Ratings vs Total 5, 4 & 2 Star Ratings</strong></br>
        <strong>To see the effects of total 5, 4 and 3 star ratings in final average ratings I created a plot. It doesn't seem to have any identical relationship. But more the upper ratings value a book has, the more it gets closer to a good ratings. Such as "Harry Potter and the Sorcerer's Stone" and "Harry Potter and the Philosopher's Stone" both have descent a amount of 5 star and 4 star ratings that results in getting an average ratings of 4.43. </strong>
    </li>
</ul>
