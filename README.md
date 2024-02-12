# 🎤🐤 AutoKanye: Kanye West automated.
autokanye is a stupid Twitter/X bot that posts random Kanye West quotes/lyrics daily. I made this in about a day to learn about the Twitter/X API.

AutoKanye is licensed under the AGPLv3 license. Read about it [here](https://www.gnu.org/licenses/agpl-3.0.en.html).

## 🤔 How does it work?
The bot uses the [kanye.rest API](https://kanye.rest) by [Andrew Jazbec (@ajzbc)](https://github.com/ajzbc) to get Kanye West quotes. The bot requests a quote, and if that quote hasn't already been posted it will post the quote and archive it (preventing the post from being posted again).
The bot continually does this daily until it runs out of quotes.

## ℹ️ Information.
> [!IMPORTANT]
> After 122 days, the bot will send a final goodbye tweet and go offline. This is due to the archival system holding every single quote in the [kanye.rest API](https://kanye.rest) API. The archival system is in place to prevent duplicate content from being posted.
> This has been implemented because duplicate posts are disallowed and I'm not going to spend hours compiling thousands of Kanye West quotes.

> [!NOTE]
> The API used in this project is the [kanye.rest API](https://kanye.rest) by [Andrew Jazbec (@ajzbc)](https://github.com/ajzbc).
> You can go check out the project at [the project's GitHub repository](https://github.com/ajzbc/kanye.rest) and Andrew himself at his [website](https://andrewjazbec.com/).
