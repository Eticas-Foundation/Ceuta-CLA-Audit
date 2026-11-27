> **DRAFT — work in progress, not the final text.** This is a working draft of the Ceuta case study by Eticas Foundation and the Institut de les Desigualtats, published ahead of the 29 November 2026 Spanish elections. It will change before the full audit is released in December 2026. The figures referred to in the text are not included in this draft; the report's own figures are in [`../report/figures/`](../report/figures/). One passage naming individual accounts has been removed because those codes have not yet been reviewed by a person (see below).

# Analysing the 2026 Ceuta Migration Crisis on X and TikTok

*Eticas Foundation and Institut de les Desigualtats — Special edition ahead of the 29 November Spanish snap elections*

## 1. Introduction

In Barcelona, the Institut de les Desigualtats, a non-governmental organization who investigates geographical, socioeconomic and gender inequalities, began hearing from young people that they were being presented with racist, sexist and xenophobic videos on social media that they never looked for. After hearing increasingly from users, the Institut wanted to someone to evidence how the algorithm shows users the content that it does and convert that evidence into practical guidance.

Together, our teams partnered for a community-led audit to look at the algorithms, product features and moderation measures TikTok and X have employed, measuring their effectives and testing how – if any – mitigate the spread of hate speech during a crisis. Our full audit, out in December 2026, compares how hate speech spread during three cases: the 2024 Southport riots in the United Kingdom, the term "gender ideology", and the 2026 Ceuta migration crisis.

Our teams decided that given the seriousness of our findings and the importance of the upcoming Spanish Snap Elections on 29 November to proactively published one excerpt from our upcoming audit. Our goal is to empower the Spanish electorate, policymakers, civil society organizations via our independent, neutral research.

## 2. Background on the 2026 Ceuta Migration Crisis

On 30 and 31 July 2026, tens of thousands of people, most of them young Moroccans and many of them minors, crossed the border from Morocco into Ceuta, a Spanish city on the North African coast, many by swimming round the Tarajal breakwater. According to the chronology of events, the crossing had been building for days on social media accounts and groups with thousands of followers. Morocco's Interior Ministry blamed digital disinformation and human-trafficking networks for the historic influx. The volume of people overwhelmed police on both sides of the border and the city's services. About 63,000 people went back to Morocco within 72 hours, though a significant number remained in Spain. By 6 August, 80 bodies had been recovered from the sea. The weeks that followed brought an intense political campaign over migration, protests, an attack by residents on a migrant camp, and a viral clip of young men with a dolphin calf on a Ceuta beach that was shared as "proof" against the whole group.

The crisis set off a firestorm of theories about how Moroccan and Spanish authorities could have missed the warning signs and disinformation campaign(s). In Spain, a national political debate polarized the public about the alleged lack of warning, the police and institutional response, and what to do with unaccompanied minors. Spain's fair-right political party used the event to reinforce its narrative of an invasion, demographic replacement and the government's surrender to Morocco. Some agitators and political organizations travelled to Ceuta to campaign. Internationally, the global far right used the case to portray the Spanish government as failing and migration as an emergency demanding tougher measures.

## 2. The Ceuta Case Study

Our teams relied on a mixed methodology for a socio-technical design: ethnographic research, stratified sampling and network analysis. Our partnership with the Institut determined, in part, our methodology based on their relationships with on the ground impacted minors, and individuals with a migration background based on their contextual knowledge of the public debates and nuance to how it had polarized the Spanish public debate.

### 2.1 Planning Phase

We had three central research questions concerning the spread of hate speech.

1. Are human and algorithmic hate speech dynamics similar, different, or mutually interdependent?
2. What does human-originated and human-spread hate speech content look like in real time on social media?
3. When human actors spread or amplify hate speech, who does the coordination necessary?

To do this at scale, our community-led audit used an LLM-as-a-judge technique: a large language model applied our definition and categories to every video, post and comment, so one definition held across two platforms and four languages.

### 2.2 Execution Phase

We used a mixture of qualitative research from our community partner that identified:

- the main actors and accounts,
- prominent contextual narratives and counternarratives to monitor in terms of the content in the tweets and TikToks we gathered,
- key terms
- hashtags, and a chronology.

The two figures below provide an overview of the main actors and accounts we monitored as well as the hashtags we monitored on TikTok specifically.

*Figure 1. An overview of the 5 main type of "actors" our team monitored as the crisis unfolded.* [Figure not included in this draft.]

*Figure 2. An overview of the key terms and hashtags measured on TikTok.* [Figure not included in this draft.]

We then incorporated that research into our technical analysis of stratified sampling, network analysis and X.

We collected 43,984 TikTok videos that name Ceuta, posted between 1 July and 30 September 2026 by 13,976 accounts and played 3.76 billion times, along with 406,573 comments and 140,170 replies.

The model classified 9,472 TikTok videos, including captions, on-screen text, a transcription of the speech and images from the video.

We collected 9,118 X posts from the same months, all naming Ceuta, from 1,428 accounts and viewed 1.95 billion times, including the most-engaged posts and the accounts, terms and hashtags our partner requested. The model classified all of them.

To classify both the TikToks and X posts, we used the United Nation's definition of hate speech according to the 2019 Strategy and Plan of Action on Hate Speech, and classified content into three categories:

- **Clearly hateful:** attacking, dehumanising or generalising negatively about people for their religion, ethnicity, race, nationality or migration status.
- **Borderline:** hostility by insinuation or policy talk ("pull factor"). Not counted as hate.
- **Not hateful:** everything else, including reporting on hate or condemning it.

*Figure 3. An overview of the 43,984 TikTok videos that name Ceuta between 1 July to 30 September 2026.* [Figure not included in this draft; see [`../report/figures/ct_methods_qa.png`](../report/figures/ct_methods_qa.png).]

### 2.3 Our Research Limitations

Although our research is reproducible, public and rigorous, we note four objective limitations for our findings.

First, we began our collection of TikTok videos on 29 September, two months after the crossings; if TikTok did remove any videos before then, then it is missing from our study. Of the videos collected, at least 175 were removed by 19 October (37 million plays), and 64 were probably gone. Too few went to tell whether hate went faster (1.1%, 3 of 280 videos with a clearly hateful caption, against 0.9% of others). We do note that the most extreme material be quickly addressed: TikTok removed 88% (July) and 100% (August) of the items Spain's Observatory on Racism and Xenophobia (OBERAXE) flagged as probably illegal in its monthly bulletins.

Second, we relied on only one large language model to classify our dataset; Claude Haiku 5.5 coded 9,145 videos in full, every caption and comment, and the themes and topics; no person hand-coded them. On Southport it agreed with a second model on 91% of posts (0.69 on a 0-to-1 agreement scale); there is no such check on TikTok videos. Speech recognition gets most Moroccan Arabic words wrong (87%, against about 6% for Spanish), so the Moroccan rate may be low. Comments, coded 100 at a time, are directional.

Third, we collected TikTok videos based on our use of TikTok's keyword search and hashtag pages, which favour videos that already did well. We estimate the corpus holds 32% of the Ceuta videos TikTok's search could return, but 70% of their plays. Therefore, small accounts are under-represented in our analysis.

Fourth, our research followed the video plays not the user accounts themselves, so our analysis does not measure if a creator's following grew because of Ceuta, our research would understate how far their videos reached. TikTok does not split plays by source (first key finding) or say whether a rewatch counts as an additional view, so "beyond the followers" counts plays. Followers are as of October 2026: for a creator who grew because of Ceuta, it understates their reach.

## 3. Findings

Following our research questions and the goal of this audit, we have clustered our findings about Ceuta into three groups of findings.

1. how human behaviour and the platforms' algorithms interacted, and what that tells us about our central research question.
2. what people and accounts posted and shared, and how their choices drove the spread of hate speech.
3. whether TikTok's and X's own product features and moderation measures slowed the spread of hate speech in practice.

### The interaction between human amplification and algorithmic amplification

Just as on X, TikTok tells us how much a video was played, but not how it was viewed: from the For You feed, a search, a hashtag or a share. So we cannot tell why anyone was shown a video. The closest we can get is to compare a TikTok's plays with other TikToks from the exact same account. Videos about Ceuta had 2.24 times more plays than the same creators' other TikToks, a finding based on 448 creators. Posting hate about Ceuta did not earn more: hateful Ceuta videos drew 0.89 times the plays of the same creators' other Ceuta videos.

*Figure 4. Each creator's Ceuta videos against their other posts. One dot per creator (448), showing plays on their Ceuta videos divided by plays on their other posts in the same weeks, on a log scale.* [See [`../report/figures/ct_within_creator.png`](../report/figures/ct_within_creator.png).]

### The human side: what people and accounts did

We found that on both platforms, within the videos and tweets classified as "clearly hateful," the narrative theme was "an invasion." 73% of the TikTok videos we classified as clearly hateful and 74% of X posts we classified as clearly hateful focused on this story. Further 8% of those TikToks and 5% of those tweets call directly for violence as a reaction to the arrival. And this was consistent across all languages and regions we measured.

*Figure 3. A visualization of the proportion of hateful videos, the plays of them, and what the main narrative was.* [See [`../report/figures/ct_themes.png`](../report/figures/ct_themes.png).]

The top of X was more hostile than the top of TikTok. 30% of X's top posts were clearly hateful, against 8.5% of TikTok's most-played videos. Part of this gap is because 28% of TikTok's most-played videos only carried Ceuta's name or hashtags on unrelated content, while every X post here is about Ceuta. Leaving the unrelated videos out, 11% of TikTok's most-played videos were clearly hateful.

Looking only at Spain and Spanish, the gap narrows. 21% of X's top posts in Spanish were clearly hateful, against 13% of TikTok's most-played videos posted from Spain. The two measures aren't identical (language on X, posting location on TikTok), but they suggest much of the overall gap comes from the English-language, largely international posts on X.

*Table 1. TikTok and the top of X under the same definition and method. Top of X: the 3,140 posts with 5,000+ likes that name Ceuta. TikTok: its most-played videos where the row says so, otherwise all coded videos. Data: data team, Ceuta on TikTok, 16 November 2026.*

| Measure | TikTok | Top of X |
|---|---|---|
| Clearly hateful (TikTok's most-played videos; X posts with 5,000+ likes) | 8.5% | 30% |
| Clearly hateful, Spanish only (TikTok: posted from Spain; X: in Spanish) | 13% | 21% |
| Borderline (same sets) | 8% | 10% |
| Plays or views on clearly hateful items | 6% | 29% |
| Plays or views on hateful and borderline items | 13% | 39% |
| Top 10 accounts' share of plays or views on clearly hateful items | 33% | 36% |
| Clearly hateful items telling the arrival as an invasion | 73% | 74% |
| Clearly hateful items calling for violence | 8% | 5% |
| Pushes back on the hostility | 7% | 5% |

We identified 76 clearly hateful TikTok videos, with 14 million plays, and 50 clearly hateful top X posts (5%) called for violence. Although we again want to caveat for any nuance, like sarcasm or humor, that our large language model could have missed in its classification. These are the model's calls and may include jokes or role-play that no person has screened out.

To our surprise our team found that within our dataset of clearly hateful videos, over a quarter of them were from official news outlets. Outlets drew 44% of all plays; they made 87 of the clearly hateful videos and drew 29% of the plays on them. [A passage naming the individual accounts with the most plays on videos the model coded clearly hateful has been removed from this public draft: those codes have not yet been reviewed by a person.] A fifth of the clearly hateful videos (22%, with 23% of their plays) were posted outside Spain and Morocco, where Ceuta became a warning: 27% of those said their own country was next.

*Figure 4. Who posted the Ceuta videos, and who drew the plays. Share of all TikTok videos in the dataset and of the plays they drew, by group. News outlets were identified by hand; "invasion vocabulary" is a word list applied to captions, not a hate code.* [See [`../report/figures/ct_reach_share.png`](../report/figures/ct_reach_share.png).]

Nearly half of the hateful content was not in the TikTok caption but in the video itself. In 48% of the clearly hateful videos, the hostility was in the speech, the on-screen text or the images. Read alone, the caption did not flag 74% of the 897 hateful videos as clearly hateful.

The comment sections crossed the border, and the hate was in the arguing. On videos posted from Morocco, 16% of comments came from accounts in Spain and 20% from the rest of Europe. In threads of 20 or more replies, 6.8% of replies were clearly hateful, against 0.3% of top comments. Replies under news outlets' videos were more often hateful (7.8% against 5.6%); outlets' videos held 55% of the replies and 63% of the hateful ones.

*Figure 5. Where the commenters were. Comments under TikTok videos posted from Spain and from Morocco, by the region TikTok gives the commenter's account. Data: data team, Ceuta on TikTok, 16 November 2026.* [See [`../report/figures/ct_comments_region.png`](../report/figures/ct_comments_region.png).]

### The platforms: do their product and moderation measures work?

**897 of 897** clearly hateful TikTok videos still public when last read · **12** carried a TikTok warning or sharing limit · **27 of 108** hashtag pages empty, though videos carry the tag

- **Hate took a bigger share of attention on X.** Clearly hateful posts drew 29% of the views on X's top posts, against 6% of the plays on TikTok's classified videos.
- **TikTok restricts some hashtags in its search function, but we found no evidence that it restricts hateful videos themselves.** 27 of 108 hashtag pages are empty when a user searches for them, yet videos with those hashtags can still be watched. They include #الانتخابات, #menas, #remigration, #haraga and #grandremplacement. The list mixes slurs with ordinary words, such as the Maghrebi word for migrants who cross irregularly and the Arabic for "the elections": it is a word list, not a hate filter. Videos carrying one of those 27 hashtags had 1.35 times their creators' usual plays. TikTok does not say which hashtags it restricts, or why.

*Table 2. TikTok hashtag pages: unlinked tags and their near-twins. The first page of each tag page on 18 October 2026, for the unlinked tags on the most videos in the dataset and the near-twins beside them. Data: data team, Ceuta on TikTok, 16 November 2026.*

| Tag | Videos on page 1 | Videos with the tag | Result |
|---|---|---|---|
| #الانتخابات ("the elections") | 0 | 33 | unlinked |
| #menas | 0 | 30 | unlinked |
| #remigration | 0 | 24 | unlinked |
| #haraga | 0 | 19 | unlinked |
| #grandremplacement | 0 | 16 | unlinked |
| #moros | 0 | 7 | unlinked |
| #greatreplacement | 0 | 5 | unlinked |
| #remigracion | 14 | 169 | returns videos |
| #reconquista | 20 | 182 | returns videos |
| #invasion | 19 | 1,211 | returns videos |
| #moro | 18 | 32 | returns videos |

- **TikTok put a warning or sharing limit on 12 of the 897 clearly hateful videos.** TikTok has a crowd-sourced fact-check feature, Footnotes, like X's Community Notes, but it has launched only in the United States, so we left it out of our analysis.
- **Most plays went beyond the creators' followers.** 53% of the plays cannot be explained by each follower watching once. Leaving out news outlets, hateful videos went as far beyond their followers as the rest (72% against 76%). But their viewers shared them more: hateful videos had a median 4.7 shares per 1,000 plays, against 2.5 for videos not coded hateful, and 1.24 times the rate of the same creators' other Ceuta videos.

*Figure 6. Share of plays beyond the creator's follower count, by creator size. For each band, the part of its plays that cannot be explained by each follower watching once. Data: data team, Ceuta on TikTok, 16 November 2026.* [See [`../report/figures/ct_size_bands.png`](../report/figures/ct_size_bands.png).]

- **Almost none of the hate had come down.** All 897 videos coded clearly hateful were public when we last read them, with 200 million plays between them; by 19 October, three of their accounts had gone and three more probably had. Our codes follow our audit's definition, not TikTok's rules; TikTok says 92% of its hate-speech removals come within a day.
- **On both platforms, a few accounts carried much of the hate.** The ten accounts with the most plays or views on clearly hateful content drew about a third of them: 33% on TikTok and 36% at the top of X.
- **Verified X accounts were over-represented in our clearly hateful sample.** Blue-check accounts posted 81% of the clearly hateful top posts, against 74% of all top posts.

TikTok surprised our research team because, just like X, it did not remove the amount of hate we assumed it would. The way TikTok mitigates hate speech is interesting. When a user searches specific hashtags on TikTok, TikTok uses the video caption to identify those hashtags and produce all of the content for that hashtags. Certain hashtags yield no search results. Our research team dug deeper to answer the question: did those videos ever exist in the first place or did no user ever use that hashtags? Because we collected all these videos, we can see that those hashtags do exist on the videos, but they do not exist when you search using that hashtag. This means that: TikTok is blocking user from searching for videos from that hashtag. The videos exist, but the user can't find them through a hateful hashtag. It's a potential suppression of hate speech, but from what we saw on total views, we didn't see any correlation between a video with a "hateful" hashtag and less views. This indicated that even if a video has a hateful hashtag, so the user can't find it via search, we don't see that translating into less total views for that video. We compare this effect to a giant room with all of the TikTok videos and content. There's a bunch of doors to access that room full of content and all the doors lead to the same place, but one of those doors is locked. Yet every other door is open and you can just walk through them and see what's behind. We found 27 hashtags unliked (i.e. the door was locked) from content.

**A note on our method.** No person on our team has yet reviewed the model's classifications, so every rate here is the model's reading, not a human verdict about any named account. We also only saw what was still online when collection began, two months after the crossings.

## 4. Impact and Recommendations

**To Spanish policymakers**

- Proactively monitor and intervene in disinformation campaigns like this.
- Monitor news outlets and the content they post during crises. Our news outlets get some of the most views per video on social media and generate what we found was the highest volume of hateful comments and replies.

**To TikTok's Trust and Safety Team**

- Monitor hateful content beyond your very narrow definition.
- Unlinking hateful content from user searches is not that effective for mitigating hate speech spreads.
- Monitor the hateful content beyond captions, within the text and images on screen, and within the speech being inset inside the video.

## 5. Conclusion and Future Outlook

In the summer of 2026, Ceuta became a story told across Europe, and on TikTok and X much of it was told as an invasion. The hate we measured came from news outlets' own headlines as well as from anonymous accounts, lived in the speech and images of videos as much as in their captions, and grew in the arguments under ordinary news reports. Almost none of it came down. What we cannot say, from outside the platforms, is why any of it was shown to anyone. That gap is itself a finding. Our full audit in December will set Ceuta beside Southport and "gender ideology".

[Placeholder - Alex to add: future outlook]
