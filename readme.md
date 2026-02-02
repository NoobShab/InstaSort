# InstaSort 
_Think shortly, sort smartly._

### InstaSort guides you on which hashtags to use to ensure you _stand out_ in the online _fitness_ crowd. 
Backed by 1000+ real-life social-media data.

This tool is recommended to fitness content creators. Creators who want to study the content in their niche and want to think productively about their next content idea -- _InstaSort_ will help them to arrange the reels with the highest engagement to the lowest in their desired hashtag. <br><br>It's the easiest way of thinking productively on what your next content will be based on the data-driven user engagements. 

#### How does _InstaSort_ operate? 
> Please check the file _projectHowTo.md_ for step by step guidance on its impementations and proper uses. 

#### What does it solve?
 > It solves the burden for fitness content creators who want to grow in social media platforms.<br><br> This tool is operated through detailed calculation of <mark>1000+</mark> fitness related content to ensure practical growth. It saves time, energy, and allows creators to be a step ahead on their content creation journey helping them to generate productive ideas based on the current trend, and identify what content actually gets users' attention.

#### What inputs does the system accept? 
1. A CSV file: containing the data for hashtags, views, likes, and engagements. 
2. Hashtag inputs. 

#### What expected outputs does it produce? 
1. Ranked lists of the reels sorted by a selected metric.
2. Metrics supported: 
    - Views
    - Likes
    - Comments
    - Engagement score


### Project Structure
* data <br>
|----> reelsArrangement.csv<br>
|----> reelsFromAccounts.csv<br>
|----> dataArrangement_csv.py<br>
|----> fitness.csv
* source<br>
|----> analyzer.cpp<br>
|----> analyzer.h<br>
|----> csvReader.h<br>
|----> csvReader.cpp<br>
|----> main.cpp<br>
|----> reel.h<br>
* readme.md <br>
* projectHowTo.md