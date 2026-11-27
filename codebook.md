# Codebook

What each code in `videos.csv` and the comments files means, how it was assigned, and the exact prompts the model was
given. The definition of hate is Southport's (*Southport on X*) word for word — the three levels, the rule that
reporting or condemning hate is not hate, and the tie-break toward `no` — with examples and a list of political actors
localised to Ceuta, so the two cases' `hateful` codes mean the same thing.

## Who coded, and how

One language model, Claude Haiku 5.5 (Anthropic), coded everything. No second model recoded the Ceuta videos and no
person hand-coded any of the corpus, not even a sample: the only videos a person watched are the ones the report shows. How much the model matters is known from Southport: recoded by Haiku 5.5 under the same
prompt, its posts agreed with the delivered codes (Claude Sonnet 5.5) on 91%, and most disagreements involved
`borderline` (report, Method). Treat the video codes as a strong first pass. The comment codes are directional: a
small model coding up to 100 items at once is a hard task.

## Videos: which were coded

Only a video whose file we held could be coded from the whole video. Of the 43,984 corpus videos, 5,671 are photo
posts (no video exists) and 725 had no usable file, leaving 37,588 (`video_file_held == "yes"`; 37,585 when the sample was drawn). The 9,472
coded videos (`coding_stratum` set) are:

- `top`: the 5,031 most-played of those — not of the whole corpus, since some photo posts and videos
  without a file had more plays;
- `random`: 1,524 drawn at random (fixed seed) from the other 32,554, each standing for 21.36
  videos (`coding_weight`);
- `walk_top100`: the remaining 2,440 Ceuta videos of the 100 most-played creators in the creator frame, for
  the within-creator comparison (no weight);
- `added_20oct`: the other 194 videos first collected on 20 October, when #CeutaNoEstaSola was added at
  Eticas's request, all coded (no weight);
- `added_4nov`: the other 282 videos first collected on 4–5 November, from the accounts and terms
  Eticas's partner named, all coded (no weight);
- `added_11nov`: the other 1 first collected on 11 November, from @davidsantosvlog, on the partner's
  list, all coded (no weight).

Weighted estimates (`top` + `random`) therefore describe the 37,585 videos with a file when the sample was drawn. Photo posts were never coded
from the video; their captions were coded on their own like every caption.

## Videos: three stages

Each sampled video was coded from what a viewer sees and reads: the caption and hashtags, the on-screen text (read from
one frame a second), a transcript where the video holds speech, and a set of frames (eight evenly spaced, plus every
frame that looks new). The model cannot hear the audio. The transcript and on-screen text it read, word for word
but masked, are in `video_content.csv`; the frames are not shipped.

**Stage 1, every sampled video: one judgement of the whole video.**

| Column | Values | Meaning |
|---|---|---|
| `hateful` | `yes` · `borderline` · `no` | Attacks, dehumanises or generalises negatively about people because of religion, ethnicity, race, nationality or migration status (`yes`, "clearly hateful"); hostile through insinuation or policy talk tied to the event (`borderline`); everything else (`no`). Headline counts use `yes` only |
| `evidence` | text | The model's own statement of what decided the code — the prompt asks for the deciding words verbatim or a short description of the image, but it is the model's choice and wording — cut at 200 characters and masked like the caption. **Blank for every video coded `no`**, so it cannot be used to look for hate the model missed |
| `stance` | `hostile` · `counter` · `neutral` · `unclear` | Hostile to migrants, Moroccans or Muslims as groups; counter-speech (defends them or pushes back) is recorded, not folded into `no` |
| `irredentist` | `yes` · `no` · `unclear` | Claims Ceuta for Morocco ("Sebta is Moroccan", "occupied Ceuta"). A territorial claim, not hate by itself |
| `call_to_action` | `violence` · `protest` · `none` | Southport's list, unchanged |

**Stage 2, only the videos judged `yes` or `borderline`: what the hostility is.** Blank, or `none`, for videos judged
`no`. Where the stage-2 prompt names a field differently, the column is given first.

| Column | Values | Meaning |
|---|---|---|
| `target` | `muslims` · `migrants_asylum` · `ethnic_racial` · `spaniards` · `other` | The main group targeted (Southport's list plus `spaniards`, reported separately) |
| `target_detail` | `moroccans_maghrebis`, `muslims`, `migrants_asylum`, `unaccompanied_minors`, `black_africans`, `amazigh`, `spaniards`, `ceutans` (Ceuta's residents as a people), `other` (`\|`-separated) | Every group targeted |
| `expressed_in` | `caption` · `on_screen_text` · `speech` · `imagery` (`\|`-separated) | Every part of the video where the hostility is expressed |
| `carrier` | one of the parts above, `multiple` or `unclear` | `expressed_in` summarised (not asked of the model) |
| `stage2_framing` (prompt: `reproduction_framing`) | `endorses` · `mocks_source` · `reports` · `condemns` · `unclear` | Whether the video adopts the hostility. Where stage 2 says anything other than `endorses`, stage 1's code stands and the video was listed for review rather than changed |
| `direction` | `anti_migrant` · `anti_moroccan` · `anti_spanish` · `anti_state` · `mixed` | Which way the hostility runs |
| `genre` | `news` · `official` · `commentary` · `mobilising` · `other` | Southport's list, unchanged |
| `format` | `news_report`, `citizen_footage`, `commentary_to_camera`, `compilation_montage`, `reaction_or_duet`, `screen_recording`, `promotional`, `music_video`, `text_card`, `other` | TikTok's production forms, kept out of `genre` |
| `media_role` | `carries_message` · `illustrates` · `unrelated` · `unclear` | Whether the pictures carry the message, illustrate the words, or are unrelated |

Stage 1 also recorded what the frames show (scene, fence or boats, uniformed personnel, children, flags); those notes
were for the model's own reading and are not shipped.

**Stage 3, only the videos judged `yes` or `borderline` (added 24 October): what the hostility says.** The same video
and model, with stage 1's verdict and evidence and stage 2's targets attached. Stage 3 never changes stage 1's code. The
list of themes was drawn up by reading about 230 of the clearly hateful videos' stage-1 and stage-2 evidence before any
theme was coded.

| Column | Values | Meaning |
|---|---|---|
| `themes` | `invasion` · `takeover` · `crime` · `sexual_threat` · `disease_filth` · `animal_cruelty` · `freeloading` · `religion_culture` · `weapon_of_morocco` · `government_blame` · `spreading` · `young_men` · `minors` · `anti_black` · `anti_spanish` · `other` (`\|`-separated) | Every story the hostility tells about the group: the arrival as an invasion; the city taken over; crime; a sexual threat; disease or dirt; cruelty to animals as typical of the group; living off others; Islam or the group's culture as a threat; Morocco sending them as a weapon; the government or NGOs to blame; Ceuta as the start of something wider; young men of military age; unaccompanied minors; hostility to Black people as such; hostility to Spaniards as a people |
| `main_theme` | one of the above | The theme that carries the hostility most |
| `forms` | `slur` · `dehumanising` · `mass_metaphor` · `mockery` · `footage_as_proof` · `fear_testimony` · `conspiracy` (`\|`-separated; blank if none) | How it is said: a slur; people as animals, vermin or filth; avalanche, wave or horde; jokes and memes; a clip presented as proof about the whole group; residents' fear presented as proof; a hidden plan behind the arrival |
| `demands` | `expel` · `force` · `protest` · `close_border` · `none` | What it asks for. `none` is dropped where another demand is listed |
| `incident` | text | The specific event the video shows or refers to, in the model's words (English, at most eight words) |
| `theme_evidence` | text | The words or image that show the main theme, cut at 200 characters and masked like the caption |

## Videos: the topic of every coded video (added 24 October)

What each coded video is about, hateful or not, and how it shows the people who crossed. Text only: the caption and
hashtags, the on-screen text, the transcript and stage 1's description of the frames; no frames were sent. The model
was told not to judge hate.

| Column | Values | Meaning |
|---|---|---|
| `topic` | `crossing` · `deaths_rescue` · `aftermath_city` · `security_returns` · `politics_spain` · `morocco_spain` · `minors` · `protest` · `solidarity` · `migrant_voices` · `unrelated` · `other` | The main subject: the entry itself; deaths and rescues; life in Ceuta afterwards; army, police and returns; Spanish politics; Morocco and relations between the two countries; unaccompanied minors; protests; support for Ceuta's residents or for the people who crossed; the people who crossed speaking for themselves; content only tagged with Ceuta |
| `topics` | the same (`\|`-separated) | Every subject it covers, the main one included |
| `migrants_portrayed` | `threat` · `victims` · `own_voice` · `crowd` · `mixed` · `not_shown` | How it shows the people who crossed |

**Too little to judge.** A video judged `no` with at most one of caption, on-screen text and transcript to read is
flagged `coding_basis_thin == True` and left out of every rate and every count.

**Not hate:** hostility toward Vox and Spanish nationalist accounts, the Spanish or Moroccan state, the Makhzen, the
King, Guardia Civil and police, Frontex, the European Union or politicians. The target must be a group defined by
religion, ethnicity, race, nationality or migration status. Hostile words from interviewees, passers-by or quoted
politicians, passed on without being adopted, are reporting (`no`); hostile wording in the video's own caption,
narration or titles counts, even from a news outlet.

## Captions on their own

`caption_hateful` (`yes` · `borderline` · `no`), set for every corpus video but 0 (the model returned no code for it):
the same definition and rules, applied to the caption and hashtags alone, 20 captions to a request, without the video,
its creator or its counts. It measures what a caption-only method would see, and it is the one code that covers every
video, so use it to follow a creator across all their posts. The caption prompt also asked for target, evidence,
stance, irredentist and genre; only `caption_hateful` ships. Applying the `caption_only` prompt below to the `caption`
column is the way to check it; the video codes cannot be redone without the videos.

## Comments

Each request held one video's comment section: its caption, a one-line summary of the video's codes, and up to 100
comments and replies, each reply under the comment it answers. Each item was coded on its own words.

| Column | Values | Meaning |
|---|---|---|
| `hateful` | `yes` · `borderline` · `no` | As above. The prompt's values are `explicit`, `insinuation` and `none`; they are stored as `yes`, `borderline` and `no` |
| `stance_to_video` | `endorses` · `disputes` · `neutral` · `off_topic` | Whether the comment agrees with the video, pushes back, neither, or is about something else |
| `mentions_feed` | `True` · `False` | The commenter says the video reached them without their seeking it ("me sale esto", "mi algoritmo"). The report counts it on top-level comments |
| `stance_to_parent` | `agrees` · `disagrees` · `neutral` · `off_topic` · `not_reply` | For a reply, against the item it answers; `not_reply` for a top-level comment |
| `counter_speech` | `True` · `False` | For a reply: it pushes back on hostility toward a group in what it answers. `False` for a top-level comment |
| `escalates` | `True` · `False` | For a reply: it is more hostile to a group than what it answers. `False` for a top-level comment |

- **`language`** in the comments files is the language TikTok tags the comment with, not the model's answer to the
  prompt's `language` field.
- **Also shipped (24 October):** `target` (the main group a hostile comment targets), `coded_language` (the language
  the model read the comment as; `ary` is Darija, which here also takes in Algerian Arabic) and, on top-level comments,
  `thread_shape` for threads with 5+ replies shown (`pile_on`, `argument`, `counter_wins`, `mixed`).
  The report's figures on whom hateful replies targeted, their language and pile-on threads rest on them.
- **Asked of the model but not shipped:** `evidence` (it quotes the comment's words).
- **Shipped since 4 November:** `stance_to_parent`, `counter_speech` and `escalates`, as the model returned them. The
  model gave reply codes to 152 top-level comments and `not_reply` to 327 replies; they
  ship as returned, so tell replies from comments by `thread_root`, not by these codes. No number in the report's text
  rests on them.
- **"The most liked comments."** The comments prompt below calls the comments it was given "the most liked comments".
  They were not: they are the first page TikTok returned (4 to 111 top-level comments a video), in
  TikTok's own order, which weighs likes and language among other things. The prompt's wording is kept as it was run.
- Comments from the earlier collection (`inherited == "yes"`) were coded like the others.
- The model never saw who wrote a comment, and the files do not say: there is no commenter column.

## The exact prompts

Word for word, as given to the model. Each prompt's version is the first 12 characters of its SHA-256: video_stage1 `71e62f4e77e7`, video_stage2 `b148bb3e4c4b`, video_stage3 `900752305a33`, video_topic `9ea82c0298b9`, caption_only `fc8a36d7e75f`, comments `6980c5f6250f`. Where a prompt's wording and the data differ, the notes above the prompts say so (field names, value names, the order of comments).

### video_stage1

```
You are coding TikTok videos about the Ceuta migration event of summer 2026 for a hate-speech audit. Facts of the case: on 30 July 2026 (Morocco's Throne Day), from late morning into the night, tens of thousands of people, most of them young Moroccans and thousands of them minors, entered the Spanish enclave of Ceuta from Morocco, mostly by swimming or walking round the breakwater at Tarajal. Spain deployed the army; most went back to Morocco within days. Over the following weeks the event became a focus for anti-migrant, anti-Moroccan and anti-Muslim mobilisation in Spain and for Moroccan claims over Ceuta ("Sebta occupied"). "Todos somos caballas" ("we are all caballas", i.e. Ceutans) is a pro-Ceuta solidarity campaign launched on 11 September; judge each use by what the video says. Videos may be in Spanish, Moroccan Darija, Modern Standard Arabic, French, English, Amazigh or other languages, and may mix them. Code hateful content matter-of-factly.

hateful: "yes" if the video attacks, dehumanises, or generalises negatively about people because of religion, ethnicity, race, nationality or migration status (e.g. Moroccans/Muslims/migrants as invaders, criminals, rapists, a threat to be removed; slurs such as "moros", "menas" used as a slur, "invasores"; blaming a whole group for crimes or disorder); "borderline" if it is hostile to a group but mainly via policy or insinuation (e.g. "efecto llamada", "esto no es inmigración", "ya sabemos quiénes son" tied to the event); "no" otherwise. Reporting on, quoting or condemning hate is "no". Hostility toward Vox and Spanish nationalist accounts, the Spanish government and state, Guardia Civil and police, Frontex, the Moroccan state, the Makhzen, King Mohammed VI, Moroccan and Spanish politicians or the European Union is NOT hateful (they are not a protected group): code "no". The target must be a group defined by religion, ethnicity, race, nationality or migration status. When unsure between "borderline" and "no", choose "no".
Interviewees, passers-by and quoted or filmed politicians are other people: passing on their hostile words without adopting them is reporting ("no"). Hostile wording in the video's own voice (its caption, narration or titles) counts, even from a news outlet. Judge the wording and the imagery, not the topic: factual reporting of numbers, crossings, deaths or returns is "no". A territorial claim ("Sebta is Moroccan", "occupied Ceuta") is not hate by itself; code it as irredentist. Hostility toward Spaniards or Ceutans as a people is coded with target = spaniards and reported separately.

Each video comes as its caption and hashtags, its on-screen text (read by OCR, so it may contain reading errors), a transcript of what is said (automatic; may be absent), and frames in time order. You cannot hear the audio.

Describe what the frames show and record the visual facts. Then judge the video as a whole:
 - hateful: yes, borderline or no, by the definition above.
 - evidence: the words that decided it, verbatim, or a short description of the image; "" when hateful is no.
 - stance: hostile (to migrants, Moroccans or Muslims as groups), counter (defends them or pushes back on hostility toward them), neutral, or unclear.
 - irredentist: yes if it claims Ceuta for Morocco ("Sebta is Moroccan", "occupied Ceuta"), no, or unclear.
 - call_to_action: violence, protest, or none.
```

### video_stage2

```
You are coding TikTok videos about the Ceuta migration event of summer 2026 for a hate-speech audit. Facts of the case: on 30 July 2026 (Morocco's Throne Day), from late morning into the night, tens of thousands of people, most of them young Moroccans and thousands of them minors, entered the Spanish enclave of Ceuta from Morocco, mostly by swimming or walking round the breakwater at Tarajal. Spain deployed the army; most went back to Morocco within days. Over the following weeks the event became a focus for anti-migrant, anti-Moroccan and anti-Muslim mobilisation in Spain and for Moroccan claims over Ceuta ("Sebta occupied"). "Todos somos caballas" ("we are all caballas", i.e. Ceutans) is a pro-Ceuta solidarity campaign launched on 11 September; judge each use by what the video says. Videos may be in Spanish, Moroccan Darija, Modern Standard Arabic, French, English, Amazigh or other languages, and may mix them. Code hateful content matter-of-factly.

hateful: "yes" if the video attacks, dehumanises, or generalises negatively about people because of religion, ethnicity, race, nationality or migration status (e.g. Moroccans/Muslims/migrants as invaders, criminals, rapists, a threat to be removed; slurs such as "moros", "menas" used as a slur, "invasores"; blaming a whole group for crimes or disorder); "borderline" if it is hostile to a group but mainly via policy or insinuation (e.g. "efecto llamada", "esto no es inmigración", "ya sabemos quiénes son" tied to the event); "no" otherwise. Reporting on, quoting or condemning hate is "no". Hostility toward Vox and Spanish nationalist accounts, the Spanish government and state, Guardia Civil and police, Frontex, the Moroccan state, the Makhzen, King Mohammed VI, Moroccan and Spanish politicians or the European Union is NOT hateful (they are not a protected group): code "no". The target must be a group defined by religion, ethnicity, race, nationality or migration status. When unsure between "borderline" and "no", choose "no".
Interviewees, passers-by and quoted or filmed politicians are other people: passing on their hostile words without adopting them is reporting ("no"). Hostile wording in the video's own voice (its caption, narration or titles) counts, even from a news outlet. Judge the wording and the imagery, not the topic: factual reporting of numbers, crossings, deaths or returns is "no". A territorial claim ("Sebta is Moroccan", "occupied Ceuta") is not hate by itself; code it as irredentist. Hostility toward Spaniards or Ceutans as a people is coded with target = spaniards and reported separately.

Each video comes as its caption and hashtags, its on-screen text (read by OCR, so it may contain reading errors), a transcript of what is said (automatic; may be absent), and frames in time order. You cannot hear the audio.

A first pass judged this video hateful or borderline; its verdict and evidence come with the video. Describe the hostility:
 - target: the main group it is hostile to; target_detail: every group it is hostile to.
 - expressed_in: every part where the hostility is expressed: caption (caption and hashtags), on_screen_text, speech (transcript), imagery (what the pictures show). In `evidence`, the deciding words verbatim for each listed part (for imagery, a short description); "" for the others.
 - reproduction_framing: endorses (adopts the hostility), mocks_source, reports (passes on other people's hostile words without adopting them), condemns, or unclear. Choose reports or condemns only if the first pass was wrong.
 - direction: anti_migrant, anti_moroccan, anti_spanish, anti_state, or mixed.
 - genre and format of the video; media_role: whether the pictures carry the message, illustrate the words, or are unrelated to them.
```

### video_stage3

```
You are coding TikTok videos about the Ceuta migration event of summer 2026 for a hate-speech audit. Facts of the case: on 30 July 2026 (Morocco's Throne Day), from late morning into the night, tens of thousands of people, most of them young Moroccans and thousands of them minors, entered the Spanish enclave of Ceuta from Morocco, mostly by swimming or walking round the breakwater at Tarajal. Spain deployed the army; most went back to Morocco within days. Over the following weeks the event became a focus for anti-migrant, anti-Moroccan and anti-Muslim mobilisation in Spain and for Moroccan claims over Ceuta ("Sebta occupied"). "Todos somos caballas" ("we are all caballas", i.e. Ceutans) is a pro-Ceuta solidarity campaign launched on 11 September; judge each use by what the video says. Videos may be in Spanish, Moroccan Darija, Modern Standard Arabic, French, English, Amazigh or other languages, and may mix them. Code hateful content matter-of-factly.

hateful: "yes" if the video attacks, dehumanises, or generalises negatively about people because of religion, ethnicity, race, nationality or migration status (e.g. Moroccans/Muslims/migrants as invaders, criminals, rapists, a threat to be removed; slurs such as "moros", "menas" used as a slur, "invasores"; blaming a whole group for crimes or disorder); "borderline" if it is hostile to a group but mainly via policy or insinuation (e.g. "efecto llamada", "esto no es inmigración", "ya sabemos quiénes son" tied to the event); "no" otherwise. Reporting on, quoting or condemning hate is "no". Hostility toward Vox and Spanish nationalist accounts, the Spanish government and state, Guardia Civil and police, Frontex, the Moroccan state, the Makhzen, King Mohammed VI, Moroccan and Spanish politicians or the European Union is NOT hateful (they are not a protected group): code "no". The target must be a group defined by religion, ethnicity, race, nationality or migration status. When unsure between "borderline" and "no", choose "no".
Interviewees, passers-by and quoted or filmed politicians are other people: passing on their hostile words without adopting them is reporting ("no"). Hostile wording in the video's own voice (its caption, narration or titles) counts, even from a news outlet. Judge the wording and the imagery, not the topic: factual reporting of numbers, crossings, deaths or returns is "no". A territorial claim ("Sebta is Moroccan", "occupied Ceuta") is not hate by itself; code it as irredentist. Hostility toward Spaniards or Ceutans as a people is coded with target = spaniards and reported separately.

Each video comes as its caption and hashtags, its on-screen text (read by OCR, so it may contain reading errors), a transcript of what is said (automatic; may be absent), and frames in time order. You cannot hear the audio.

A first pass judged this video hateful or borderline; its verdict, its evidence and the groups it targets come with the video. Name what the hostility says about the group, how it says it and what it asks for. List only what the video itself does, in its own voice or by the way it uses other people's words and pictures.
 - themes: every story it tells about the group. invasion (the arrival as an invasion, assault, attack or conquest of Ceuta, Spain or Europe); takeover (they have taken the streets, beaches, parks, homes or services: the city is no longer ours); crime (theft, looting, break-ins or squatting, assaults, stabbings, gangs, criminal pasts, released prisoners); sexual_threat (rape, sexual assault or harassment of women or girls); disease_filth (disease, dirt, smell, excrement, rubbish); animal_cruelty (harming animals, presented as typical of the group); freeloading (benefits, free housing or services, not working, expensive phones, living off taxpayers); religion_culture (Islam or their culture as incompatible or a threat: women, veils, terrorism, the Reconquista); weapon_of_morocco (Morocco, its state or its King sent them as a weapon: hybrid war, pressure on Spain, a fifth column); government_blame (the Spanish government, the left, NGOs or the EU let them in or protect them, tied to hostility to the group: betrayal, "new voters", regularisation); spreading (Ceuta is the start: the rest of Spain, Europe or another country is next; the population is being replaced); young_men (the arrivals as young men of military age, with no women or families); minors (unaccompanied minors as a threat or a burden); anti_black (hostility to Black or sub-Saharan people as such); anti_spanish (hostility to Spaniards or Ceutans as a people); other.
 - main_theme: the one theme that carries the hostility most.
 - forms: how it is said, every one that applies. slur (an ethnic or religious slur); dehumanising (animals, vermin, plague, parasites, zombies or filth as a metaphor for people); mass_metaphor (avalanche, flood, waves, tide, hordes, swarm); mockery (jokes, memes, parody or ridicule); footage_as_proof (a clip presented as proof of a claim about the whole group); fear_testimony (residents' fear or distress presented as proof); conspiracy (a hidden plan or orchestrator behind the arrival).
 - demands: what it asks for, every one that applies. expel (expel, deport or send back all of them, "fuera"); force (the army, armed force, beatings, shooting, vigilantes); protest (rallies, marches, camps); close_border (walls, closing the border, no more entries); none.
 - incident: the specific event it shows or refers to, if any, in at most eight words of English ("a dolphin calf killed on a beach", "young men entering a building at night"); "" if none.
 - theme_evidence: the words or the image that show the main theme, verbatim, at most 30 words.
```

### video_topic

```
You are coding TikTok videos about the Ceuta migration event of summer 2026 for a hate-speech audit. Facts of the case: on 30 July 2026 (Morocco's Throne Day), from late morning into the night, tens of thousands of people, most of them young Moroccans and thousands of them minors, entered the Spanish enclave of Ceuta from Morocco, mostly by swimming or walking round the breakwater at Tarajal. Spain deployed the army; most went back to Morocco within days. Over the following weeks the event became a focus for anti-migrant, anti-Moroccan and anti-Muslim mobilisation in Spain and for Moroccan claims over Ceuta ("Sebta occupied"). "Todos somos caballas" ("we are all caballas", i.e. Ceutans) is a pro-Ceuta solidarity campaign launched on 11 September; judge each use by what the video says. Videos may be in Spanish, Moroccan Darija, Modern Standard Arabic, French, English, Amazigh or other languages, and may mix them. Code hateful content matter-of-factly.

Each video comes as its caption and hashtags, its on-screen text (read by OCR, so it may contain reading errors), a transcript of what is said (automatic; may be absent) and a first pass's description of its frames. Say what the video is about and how it shows the people who crossed. Do not judge whether it is hateful.
 - topic: the main subject. crossing (the entry itself: swimmers, the breakwater, the fence, crowds arriving); deaths_rescue (bodies, drownings, rescues, the missing, injuries); aftermath_city (life in Ceuta afterwards: streets, camps, beaches, shelters, residents' experience); security_returns (the army, police and Guardia Civil, returns, border control); politics_spain (the Spanish government, parties, parliament, politicians' statements); morocco_spain (the Moroccan state, relations between the two countries, claims over Ceuta and Melilla, Morocco's role); minors (unaccompanied minors: their care, numbers, transfers); protest (rallies, marches or camps about the event); solidarity (support for Ceuta's residents or for the people who crossed, donations, "Todos somos caballas"); migrant_voices (the people who crossed speaking for themselves: motives, journeys, life after); unrelated (only tagged or captioned with Ceuta: entertainment, sport, travel, other news); other.
 - topics: every subject it covers, the main one included.
 - migrants_portrayed: how it shows the people who crossed. threat (dangerous, criminal, invaders); victims (suffering, exploited, in danger); own_voice (speaking for themselves); crowd (a mass, without comment either way); mixed; not_shown (absent, or not a subject).
```

### caption_only

```
You are coding TikTok videos about the Ceuta migration event of summer 2026 for a hate-speech audit. Facts of the case: on 30 July 2026 (Morocco's Throne Day), from late morning into the night, tens of thousands of people, most of them young Moroccans and thousands of them minors, entered the Spanish enclave of Ceuta from Morocco, mostly by swimming or walking round the breakwater at Tarajal. Spain deployed the army; most went back to Morocco within days. Over the following weeks the event became a focus for anti-migrant, anti-Moroccan and anti-Muslim mobilisation in Spain and for Moroccan claims over Ceuta ("Sebta occupied"). "Todos somos caballas" ("we are all caballas", i.e. Ceutans) is a pro-Ceuta solidarity campaign launched on 11 September; judge each use by what the video says. Videos may be in Spanish, Moroccan Darija, Modern Standard Arabic, French, English, Amazigh or other languages, and may mix them. Code hateful content matter-of-factly.

hateful: "yes" if the caption attacks, dehumanises, or generalises negatively about people because of religion, ethnicity, race, nationality or migration status (e.g. Moroccans/Muslims/migrants as invaders, criminals, rapists, a threat to be removed; slurs such as "moros", "menas" used as a slur, "invasores"; blaming a whole group for crimes or disorder); "borderline" if it is hostile to a group but mainly via policy or insinuation (e.g. "efecto llamada", "esto no es inmigración", "ya sabemos quiénes son" tied to the event); "no" otherwise. Reporting on, quoting or condemning hate is "no". Hostility toward Vox and Spanish nationalist accounts, the Spanish government and state, Guardia Civil and police, Frontex, the Moroccan state, the Makhzen, King Mohammed VI, Moroccan and Spanish politicians or the European Union is NOT hateful (they are not a protected group): code "no". The target must be a group defined by religion, ethnicity, race, nationality or migration status. When unsure between "borderline" and "no", choose "no".
Interviewees, passers-by and quoted politicians are other people: passing on their hostile words without adopting them is reporting ("no"). Hostile wording in the caption's own voice counts, even from a news outlet. Judge the wording, not the topic: factual reporting of numbers, crossings, deaths or returns is "no". A territorial claim ("Sebta is Moroccan", "occupied Ceuta") is not hate by itself; code it as irredentist. Hostility toward Spaniards or Ceutans as a people is coded with target = spaniards and reported separately.

You are given the captions and hashtags of TikTok videos, one per line as {"id", "date", "text"}. You do not see the videos, who posted them or their counts. Code each caption on its own words. For every id:
 - hateful: yes, borderline or no, by the definition above.
 - target: the group it is hostile to (moroccans_maghrebis, muslims, migrants_asylum, unaccompanied_minors, black_africans, spaniards, other), or none when hateful is no.
 - evidence: the words that decided it, verbatim, when hateful is not no; otherwise "".
 - stance: hostile (to migrants, Moroccans or Muslims as groups), counter (defends them or pushes back on hostility toward them), neutral, or unclear.
 - irredentist: yes if it claims Ceuta for Morocco, no, or unclear.
 - genre: news, official, commentary, mobilising, or other.
Return every id given, once, in "codes".
```

### comments

```
You are coding TikTok videos about the Ceuta migration event of summer 2026 for a hate-speech audit.
Facts of the case: on 30 July 2026 (Morocco's Throne Day), from late morning into the night, tens of thousands of
people, most of them young Moroccans and thousands of them minors, entered the Spanish enclave of Ceuta from
Morocco, mostly by swimming or walking round the breakwater at Tarajal. Spain deployed the army; most went back
to Morocco within days. Over the following weeks the event became a focus for anti-migrant, anti-Moroccan and
anti-Muslim mobilisation in Spain and for Moroccan claims over Ceuta ("Sebta occupied"). "Todos somos caballas"
("we are all caballas", i.e. Ceutans) is a pro-Ceuta solidarity campaign launched on 11 September; judge each use
by what the video says. Videos may be in Spanish, Moroccan Darija, Modern Standard Arabic, French, English, Amazigh
or other languages, and may mix them. Code hateful content matter-of-factly.

hateful: "yes" if the comment attacks, dehumanises, or generalises negatively about people because of religion, ethnicity, race, nationality or migration status (e.g. Moroccans/Muslims/migrants as invaders, criminals, rapists, a threat to be removed; slurs such as "moros", "menas" used as a slur, "invasores"; blaming a whole group for crimes or disorder); "borderline" if it is hostile to a group but mainly via policy or insinuation (e.g. "efecto llamada", "esto no es inmigración", "ya sabemos quiénes son" tied to the event); "no" otherwise. Reporting on, quoting or condemning hate is "no". Hostility toward Vox and Spanish nationalist accounts, the Spanish government and state, Guardia Civil and police, Frontex, the Moroccan state, the Makhzen, King Mohammed VI, Moroccan and Spanish politicians or the European Union is NOT hateful (they are not a protected group): code "no". The target must be a group defined by religion, ethnicity, race, nationality or migration status. When unsure between "borderline" and "no", choose "no".
Judge the wording, not the topic: factual reporting of numbers, crossings, deaths or returns is "no". A territorial claim ("Sebta is Moroccan", "occupied Ceuta") is not hate by itself. Hostility toward Spaniards or Ceutans as a people is coded with target = spaniards.

You are given ONE TikTok video's comment section: the video's caption and hashtags, a one-line summary of how the
video itself was coded (or "video not coded"), then comments, each with the replies held under it indented below it.
Each line is {"id", "text"}; a reply may carry "to": the id of the reply it answers (by @-mention); otherwise it
answers the comment above it. You do not see who wrote anything, their counts or the video itself. These are the most
liked comments and the first page of replies under the most-argued ones, not the whole section.

Code EVERY item (comment or reply) on its own words, using the caption, the video summary and what it answers only to
understand what it means:
 hateful           "none" ("no" above), "insinuation" ("borderline" above: hostile to the group by implication only)
                   or "explicit" ("yes" above); a comment that quotes hate in order to reject it is none
 target            the group it is hostile to: moroccans_maghrebis, muslims, migrants_asylum, unaccompanied_minors,
                   black_africans, spaniards, other; "none" when hateful is none
 evidence          the words that decided it, verbatim, when hateful is not none; otherwise ""
 mentions_feed     true if it says the video reached them without their seeking it ("me sale esto", "mi algoritmo",
                   "why is this on my For You page"), else false
 language          es, ar (Modern Standard Arabic), ary (Darija, in Arabic or Latin letters), fr, en or other;
                   "none" for emoji or tags only
 stance_to_video   endorses, disputes, neutral, or off_topic (about something else, or only tags or emoji)
For a REPLY also code, against the item it answers (for a comment use "not_reply" and false):
 stance_to_parent  agrees, disagrees, neutral, off_topic
 counter_speech    true if it pushes back on hostility toward a group in what it answers, else false
 escalates         true if it is more hostile to a group than what it answers, else false
Then for every comment with 5 or more replies shown, code the thread as a whole:
 thread_shape      pile_on (replies mostly join in), argument (replies split and argue), counter_wins (pushback
                   dominates a hostile comment), mixed (none of these clearly)
Return every item id given, once, in "items", and one entry per such thread in "threads".
```

## What followed each prompt

The templates below were filled in for each request (`{...}` marks a value). A video request was `message_video`, then each frame as `message_video_frame` followed by the image, then the closing line for stage 1, 2 or 3 (stage 3 adds stage 2's targets, joined by commas). A topic request was `message_topic` alone, with stage 1's description of the frames in place of the frames. A comment request was `message_comments`, with `message_video_summary` filled from the video's codes. A caption request was `message_captions`, 20 captions at a time.

### message_video

```
CAPTION AND HASHTAGS{caption_cut}:
{caption}
{hashtags}

ON-SCREEN TEXT (OCR, seconds on screen){ocr_cut}:
{ocr}

TRANSCRIPT ({transcript_status}){transcript_cut}:
{transcript}

FRAMES ({n_frames}, video length {duration_s}s):
```

### message_video_frame

```
frame at {t:.1f}s
```

### message_video_stage1_close

```
Judge this video. Return the JSON object.
```

### message_video_stage2_close

```
First pass: hateful = {hateful}; evidence: {evidence}
Describe the hostility in this video. Return the JSON object.
```

### message_video_stage3_close

```
First pass: hateful = {hateful}; evidence: {evidence}; targets: {targets}
Name the themes, forms and demands of the hostility in this video. Return the JSON object.
```

### message_topic

```
CAPTION AND HASHTAGS{caption_cut}:
{caption}
{hashtags}

ON-SCREEN TEXT (OCR, seconds on screen){ocr_cut}:
{ocr}

TRANSCRIPT ({transcript_status}){transcript_cut}:
{transcript}

FRAMES, AS DESCRIBED BY A FIRST PASS (video length {duration_s}s):
{scene}

Say what this video is about. Return the JSON object.
```

### message_comments

```
CAPTION AND HASHTAGS:
{caption}
{hashtags}

VIDEO: {video_summary}

COMMENTS ({n_items} items):
{items}

Code every item. Return the JSON object.
```

### message_video_summary

```
video coded hateful={hateful}, stance={stance}, target={target}, direction={direction}, genre={genre}; scene: {scene}
```

### message_captions

```
CAPTIONS ({n_items}):
{items}

Code every caption. Return the JSON object.
```

## X posts (report Section 7): the exact prompts

The posts in `x_posts.csv` were coded by the same model (Claude Haiku 5.5) on Ceuta's delivered video prompts, reworded for posts: stage 1 for every post, stage 3 for the hateful and borderline ones (there is no stage 2 on X). Versions: x_stage1 `61a02446c351`, x_stage3 `06c52d7e4a0d`. The model saw the post's text and images (a video's preview frame only) and, for a quote or reply, the post it points to.

### x_stage1

```
You are coding X (Twitter) posts about the Ceuta migration event of summer 2026 for a hate-speech audit. Facts of the case: on 30 July 2026 (Morocco's Throne Day), from late morning into the night, tens of thousands of people, most of them young Moroccans and thousands of them minors, entered the Spanish enclave of Ceuta from Morocco, mostly by swimming or walking round the breakwater at Tarajal. Spain deployed the army; most went back to Morocco within days. Over the following weeks the event became a focus for anti-migrant, anti-Moroccan and anti-Muslim mobilisation in Spain and for Moroccan claims over Ceuta ("Sebta occupied"). "Todos somos caballas" ("we are all caballas", i.e. Ceutans) is a pro-Ceuta solidarity campaign launched on 11 September; judge each use by what the post says. Posts may be in Spanish, Moroccan Darija, Modern Standard Arabic, French, English, Amazigh or other languages, and may mix them. Code hateful content matter-of-factly.

hateful: "yes" if the post attacks, dehumanises, or generalises negatively about people because of religion, ethnicity, race, nationality or migration status (e.g. Moroccans/Muslims/migrants as invaders, criminals, rapists, a threat to be removed; slurs such as "moros", "menas" used as a slur, "invasores"; blaming a whole group for crimes or disorder); "borderline" if it is hostile to a group but mainly via policy or insinuation (e.g. "efecto llamada", "esto no es inmigración", "ya sabemos quiénes son" tied to the event); "no" otherwise. Reporting on, quoting or condemning hate is "no". Hostility toward Vox and Spanish nationalist accounts, the Spanish government and state, Guardia Civil and police, Frontex, the Moroccan state, the Makhzen, King Mohammed VI, Moroccan and Spanish politicians or the European Union is NOT hateful (they are not a protected group): code "no". The target must be a group defined by religion, ethnicity, race, nationality or migration status. When unsure between "borderline" and "no", choose "no".
Quoted, filmed or pictured people and politicians are other people: passing on their hostile words without adopting them is reporting ("no"). Hostile wording in the post's own voice (its text, or words its author put on an image) counts, even from a news outlet. Judge the wording and the imagery, not the topic: factual reporting of numbers, crossings, deaths or returns is "no". A territorial claim ("Sebta is Moroccan", "occupied Ceuta") is not hate by itself; code it as irredentist. Hostility toward Spaniards or Ceutans as a people is coded with target = spaniards and reported separately.

Each post comes as its date, its full text, its images if any (for a video or GIF, only its preview frame) and, when it quotes or replies to another post, that other post's text, marked as such. You do not see who posted it or its counts. Code the post on its own words and images: the other post is context, and hostile words in it count only if the post adopts or endorses them.

Judge the post as a whole:
 - hateful: yes, borderline or no, by the definition above.
 - evidence: the words that decided it, verbatim, or a short description of the image; "" when hateful is no.
 - target: the group it is hostile to (moroccans_maghrebis, muslims, migrants_asylum, unaccompanied_minors, black_africans, spaniards, other), or none when hateful is no.
 - stance: hostile (to migrants, Moroccans or Muslims as groups), counter (defends them or pushes back on hostility toward them), neutral, or unclear.
 - irredentist: yes if it claims Ceuta for Morocco ("Sebta is Moroccan", "occupied Ceuta"), no, or unclear.
 - call_to_action: violence, protest, or none.
 - genre: news, official, commentary, mobilising, or other.
```

### x_stage3

```
You are coding X (Twitter) posts about the Ceuta migration event of summer 2026 for a hate-speech audit. Facts of the case: on 30 July 2026 (Morocco's Throne Day), from late morning into the night, tens of thousands of people, most of them young Moroccans and thousands of them minors, entered the Spanish enclave of Ceuta from Morocco, mostly by swimming or walking round the breakwater at Tarajal. Spain deployed the army; most went back to Morocco within days. Over the following weeks the event became a focus for anti-migrant, anti-Moroccan and anti-Muslim mobilisation in Spain and for Moroccan claims over Ceuta ("Sebta occupied"). "Todos somos caballas" ("we are all caballas", i.e. Ceutans) is a pro-Ceuta solidarity campaign launched on 11 September; judge each use by what the post says. Posts may be in Spanish, Moroccan Darija, Modern Standard Arabic, French, English, Amazigh or other languages, and may mix them. Code hateful content matter-of-factly.

hateful: "yes" if the post attacks, dehumanises, or generalises negatively about people because of religion, ethnicity, race, nationality or migration status (e.g. Moroccans/Muslims/migrants as invaders, criminals, rapists, a threat to be removed; slurs such as "moros", "menas" used as a slur, "invasores"; blaming a whole group for crimes or disorder); "borderline" if it is hostile to a group but mainly via policy or insinuation (e.g. "efecto llamada", "esto no es inmigración", "ya sabemos quiénes son" tied to the event); "no" otherwise. Reporting on, quoting or condemning hate is "no". Hostility toward Vox and Spanish nationalist accounts, the Spanish government and state, Guardia Civil and police, Frontex, the Moroccan state, the Makhzen, King Mohammed VI, Moroccan and Spanish politicians or the European Union is NOT hateful (they are not a protected group): code "no". The target must be a group defined by religion, ethnicity, race, nationality or migration status. When unsure between "borderline" and "no", choose "no".
Quoted, filmed or pictured people and politicians are other people: passing on their hostile words without adopting them is reporting ("no"). Hostile wording in the post's own voice (its text, or words its author put on an image) counts, even from a news outlet. Judge the wording and the imagery, not the topic: factual reporting of numbers, crossings, deaths or returns is "no". A territorial claim ("Sebta is Moroccan", "occupied Ceuta") is not hate by itself; code it as irredentist. Hostility toward Spaniards or Ceutans as a people is coded with target = spaniards and reported separately.

Each post comes as its date, its full text, its images if any (for a video or GIF, only its preview frame) and, when it quotes or replies to another post, that other post's text, marked as such. You do not see who posted it or its counts. Code the post on its own words and images: the other post is context, and hostile words in it count only if the post adopts or endorses them.

A first pass judged this post hateful or borderline; its verdict, its evidence and the groups it targets come with the post. Name what the hostility says about the group, how it says it and what it asks for. List only what the post itself does, in its own voice or by the way it uses other people's words and images.
 - themes: every story it tells about the group. invasion (the arrival as an invasion, assault, attack or conquest of Ceuta, Spain or Europe); takeover (they have taken the streets, beaches, parks, homes or services: the city is no longer ours); crime (theft, looting, break-ins or squatting, assaults, stabbings, gangs, criminal pasts, released prisoners); sexual_threat (rape, sexual assault or harassment of women or girls); disease_filth (disease, dirt, smell, excrement, rubbish); animal_cruelty (harming animals, presented as typical of the group); freeloading (benefits, free housing or services, not working, expensive phones, living off taxpayers); religion_culture (Islam or their culture as incompatible or a threat: women, veils, terrorism, the Reconquista); weapon_of_morocco (Morocco, its state or its King sent them as a weapon: hybrid war, pressure on Spain, a fifth column); government_blame (the Spanish government, the left, NGOs or the EU let them in or protect them, tied to hostility to the group: betrayal, "new voters", regularisation); spreading (Ceuta is the start: the rest of Spain, Europe or another country is next; the population is being replaced); young_men (the arrivals as young men of military age, with no women or families); minors (unaccompanied minors as a threat or a burden); anti_black (hostility to Black or sub-Saharan people as such); anti_spanish (hostility to Spaniards or Ceutans as a people); other.
 - main_theme: the one theme that carries the hostility most.
 - forms: how it is said, every one that applies. slur (an ethnic or religious slur); dehumanising (animals, vermin, plague, parasites, zombies or filth as a metaphor for people); mass_metaphor (avalanche, flood, waves, tide, hordes, swarm); mockery (jokes, memes, parody or ridicule); footage_as_proof (a video or image presented as proof of a claim about the whole group); fear_testimony (residents' fear or distress presented as proof); conspiracy (a hidden plan or orchestrator behind the arrival).
 - demands: what it asks for, every one that applies. expel (expel, deport or send back all of them, "fuera"); force (the army, armed force, beatings, shooting, vigilantes); protest (rallies, marches, camps); close_border (walls, closing the border, no more entries); none.
 - incident: the specific event it shows or refers to, if any, in at most eight words of English ("a dolphin calf killed on a beach", "young men entering a building at night"); "" if none.
 - theme_evidence: the words or the image that show the main theme, verbatim, at most 30 words.
```

