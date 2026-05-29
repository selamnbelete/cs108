# CS 108 Lab — The Shape of Language: Visualizing Words and Their Relationships

**Name:** _______________________________ **Date:** _____________

---

## Submission

> Submit only [OBSERVE] questions. Do not submit [REFLECT]s!!

---

## Overview

A word alone means almost nothing. Words mean things through their relationships —
to other words, to the communities that use them, to the moment in time when they
appear. A linguist studying a community doesn't just count words; they map the
structure of language itself.

In this lab you will build four tools that make that structure visible. Each one
takes the same raw material — post titles scraped from Reddit — and asks a
fundamentally different question about what language reveals.

1. **Co-occurrence Graph** — which words travel together? Force-directed graph of
   word pairs that appear in the same post title
2. **Word Shift** — what vocabulary separates two communities? A divergence chart
   showing which words belong to one subreddit and not the other
3. **Bubble Cloud** — what does a community talk about, and how are those topics
   connected? A physical word cloud where hovering reveals hidden co-occurrence links
4. **Semantic Timeline** — how does a community's vocabulary shift over hours?
   A stream graph of word frequency across time buckets

All four tools run entirely in the browser. However, you can't open them directly.

```bash
cd /path/to/your/words/folder
python -m http.server 8000
```

Then open http://localhost:8000/<FILENAME>.html in your browser instead of double-clicking the file.

**For example:** Open http://localhost:8000/cooccurrence_graph.html in your browser instead of double-clicking the file.

---

## Part 1: Co-occurrence Graph

### Background

Two words **co-occur** when they appear in the same sentence, title, or document.
Co-occurrence is not just about frequency — it is about *structure*. Words that
always travel together reveal conceptual bundling: ideas the community treats as
inseparable. Words that appear frequently but rarely with each other reveal distinct
conversational threads running in parallel.

In this tool, each word is a node. Each co-occurrence relationship is an edge,
with thickness proportional to how often the pair appears together. Node size
and color encode how often the word appears across all post titles. The D3 force
simulation spaces nodes so that tightly connected clusters pull together and
isolated words drift to the edges.

This structure is called a **word co-occurrence network** and is used in
computational linguistics, topic modeling, and knowledge graph construction.

### The Tool

If you haven't already, run

```bash
cd /path/to/your/words/folder
python -m http.server 8000
```

Then open http://localhost:8000/cooccurrence_graph.html in your browser instead of double-clicking the file.


Enter a subreddit and click **Build Graph**.
Drag nodes to rearrange. Click any node to see its neighbors ranked by
co-occurrence frequency, and example post titles in the sidebar.

**[OBSERVE1]** Look at the graph before clicking anything. Are there distinct
clusters of words, or does the graph look like one tangled mass? Describe
the large-scale structure you see — how many rough "regions" can you identify,
and what do the words in each region seem to have in common?

&nbsp;

&nbsp;

&nbsp;

**[OBSERVE2]** Click the node with the most connections (the largest, most central
node). List its top five co-occurring words from the sidebar. Do those neighbors
connect primarily to each other, or do they branch out to other parts of the
graph? What does that pattern suggest about this word's role in the community's
discourse?

&nbsp;

&nbsp;

&nbsp;

**[OBSERVE3]** Find a word that sits at the periphery — small, few connections,
far from the center. Click it. How many co-occurring neighbors does it have?
Read one of the example posts in the sidebar. Is this word a niche topic, a
proper noun, or something else? What would it take for a word to move from the
periphery to the center of a co-occurrence graph?

&nbsp;

&nbsp;

**[REFLECT]** Co-occurrence measures which words appear *together*, not which
words mean the same thing. "Good" and "bad" could easily co-occur in a debate.
"Cancer" and "treatment" co-occur constantly in medical subreddits. What
would you need beyond co-occurrence to understand whether two co-occurring
words are allied or opposed?

&nbsp;

&nbsp;

---

## Part 2: Word Shift

### Background

Every community has its own dialect — words it uses more than outsiders do,
topics it returns to obsessively, framings it takes for granted. The **word shift**
visualization makes this dialect visible by comparing two communities
word-by-word.

The technical measure is the **log-ratio** of relative frequencies:

```
shift_score(w) = log( freq_A(w) / freq_B(w) )
```

A large positive score means the word is much more common in community A.
A large negative score means it belongs to B. Words near zero are shared
vocabulary. The chart ranks words from most-A at the top to most-B at the
bottom, with bar length showing how extreme the difference is.

This technique is used in political science (comparing party platforms),
cultural analytics (comparing eras of literature), and social media research.

### The Tool

If you haven't already, run

```bash
cd /path/to/your/words/folder
python -m http.server 8000
```

Then open http://localhost:8000/word_shift.html in your browser instead of double-clicking the file.


Enter two subreddit names and click **Compare**.
The chart will rank the most divergent words. Click any word or bar to see
how often it appears in each community and which posts contain it.

**[OBSERVE4]** Use the default `r/science` vs `r/technology`. List the top
three words most associated with each community. Do they confirm your prior
expectations about what each subreddit talks about, or do any surprise you?

&nbsp;

&nbsp;

&nbsp;

**[OBSERVE5]** Click a word that strongly belongs to one community. Read the
example posts in the sidebar for *both* communities. Does the word appear in
completely different contexts on each side, or does it genuinely just appear
more in one place?

&nbsp;

&nbsp;

&nbsp;

**[OBSERVE6]** Replace one or both subreddit(s) with a very different community:
try `r/politics` vs `r/investing`, or `r/cooking` vs `r/fitness`. Which
words sit closest to the center (shared vocabulary)? What does shared
vocabulary between two different communities reveal about common ground?

&nbsp;

&nbsp;

**[REFLECT]** The log-ratio treats all words equally — a rare word that appears
twice in A and zero times in B gets the same maximum score as a common word that
appears 50 times in A and 1 time in B. Is that fair? What are the tradeoffs of
weighting by raw frequency versus normalized frequency?

&nbsp;

&nbsp;

---

## Part 3: Bubble Cloud

### Background

A classic word cloud encodes one thing: frequency. A bigger bubble means a more
common word. But frequency alone erases all relationships — it cannot tell you
that "climate" and "policy" always appear together while "climate" and "sports"
never do.

This tool adds a second layer: **co-occurrence on demand**. When you hover a
bubble, the visualization reveals lines connecting it to every word that has
appeared in the same post title. The lines stay hidden by default to keep the
display clean — you pull the structure into view one word at a time.

Clicking pins a word in place, keeping its connections visible while you
explore the rest of the cloud. This is an example of **progressive disclosure**:
showing complexity only when the user asks for it.

### The Tool

If you haven't already, run

```bash
cd /path/to/your/words/folder
python -m http.server 8000
```

Then open http://localhost:8000/bubble_cloudhtml in your browser instead of double-clicking the file.


Enter a subreddit and click **Build Cloud**.
Hover bubbles to reveal co-occurrence links. Click to pin a word; click
again or press **Unpin** to release it.

**[OBSERVE7]** Pick the three largest bubbles and hover each one in turn.
Describe the difference in their co-occurrence patterns. Does a larger
bubble necessarily have more co-occurring partners, or can a frequent word
be surprisingly isolated?

&nbsp;

&nbsp;

&nbsp;

**[OBSERVE8]** Find two bubbles that are physically close to each other in
the layout. Hover each one. Do they share co-occurring neighbors, or are
they spatially close by coincidence? (The force simulation clusters bubbles
by frequency, not by meaning — so spatial proximity is not guaranteed to
mean semantic similarity.)

&nbsp;

&nbsp;

&nbsp;

**[OBSERVE9]** Pin a word that interests you and count how many lines
appear. Now hover a neighbor word without unpinning. Can you identify a
"bridge" word — one that connects two otherwise unrelated clusters? Describe
the bridge word and the two clusters it connects.

&nbsp;

&nbsp;

**[REFLECT]** This tool hides complexity until you ask for it (progressive
disclosure). Compare that to the co-occurrence *graph* in Part 1, which shows
all edges simultaneously. What does each approach make easy to see, and what
does each approach make hard to see? Is there a task where one is clearly
better than the other?

&nbsp;

&nbsp;

---

## Part 4: Semantic Timeline

### Background

Language is not static. A community's vocabulary shifts hour by hour as news
breaks, discussions start and die, and topics rise and fall. The **semantic
timeline** makes this drift visible by bucketing posts into time windows and
tracking how word frequency changes across windows.

The display is a **stream graph** — a variant of the stacked area chart where
the baseline floats to minimize visual wiggle (this is called the *wiggle
offset* in D3). Each colored band represents one word; the band's thickness
at any horizontal position shows how active that word was during that time
bucket. Wider bands mean the word dominated conversations at that moment.

The bottom panel shows the actual posts behind any band you hover,
with the tracked word highlighted. This closes the loop between abstraction
(the stream) and the raw data (the posts).

### The Tool

If you haven't already, run

```bash
cd /path/to/your/words/folder
python -m http.server 8000
```

Then open http://localhost:8000/semantic_timeline.html in your browser instead of double-clicking the file.

Enter a subreddit and click **Build Timeline**.
The tool fetches `/new` (most recent posts) to get time-stamped data, buckets
them into the interval you choose, and builds the stream graph.

Hover a band to preview posts; click to isolate that word. Use the legend
panel to toggle individual words.

**[OBSERVE10]** Look at the stream graph before interacting with it. Are there
bands that are consistently wide across all time buckets, or do you see bands
that spike briefly and disappear? Describe the overall shape of the stream —
is it chaotic or does it show a clear dominant topic?

&nbsp;

&nbsp;

&nbsp;

**[OBSERVE11]** Click the widest band (the most dominant word). Read the posts
in the bottom panel. Are they all about the same event, or does this word
appear in posts about many unrelated topics? What does that tell you about
whether the word is a *content* word (tied to one story) or a *function*
word (used in many different contexts)?

&nbsp;

&nbsp;

&nbsp;

**[OBSERVE12]** Switch to a different subreddit and change the bucket
size to **2-hour**. Find a word whose band gets wider or narrower over time.
Look at the posts from its widest bucket versus its narrowest. Can you
identify a specific event or story that caused the spike?

&nbsp;

&nbsp;

**[REFLECT]** This tool uses only the post *titles* — not the body text, not
the comments. A major news story might generate hundreds of comments but only
a few post titles. What aspects of a community's language would you miss
entirely by looking only at titles? What aspects would titles capture
*better* than comments?

&nbsp;

&nbsp;

---

## Part 5: Semantic Field Mapper

### Background

Every word belongs to a **semantic field** — a cluster of words that share
a conceptual domain. "War," "battle," and "siege" all belong to the field
of *conflict*. "Cell," "gene," and "cancer" all belong to *body and health*.
When you count how many words from each semantic field appear in a
community's post titles, you get a rough fingerprint of what that
community *thinks and talks about* at the level of meaning rather than
individual words.

The display is a **radar chart** (also called a spider chart): each of the
twelve semantic fields occupies one axis, radiating out from the center.
The further a vertex stretches along an axis, the more words from that
field appeared in the community's posts. Two communities are overlaid on
the same chart, so you can see their conceptual profiles simultaneously —
where the polygons diverge is where the communities differ most deeply.

The twelve fields are: **Conflict, Body & Health, Money & Economy,
Technology, Nature & Environment, Politics & Power, Emotion & Self,
Science & Discovery, Time & Change, Society & Culture, Place & Geography,**
and **Work & Production**.

### The Tool

If you haven't already, run

```bash
cd /path/to/your/words/folder
python -m http.server 8000
```

Then open http://localhost:8000/semantic_radar.html in your browser instead of double-clicking the file.

Enter two subreddit names and click **Compare**. The radar chart renders immediately. 

Click any field label
or axis dot to see the breakdown in the sidebar: how strongly each
community scores on that field, and exactly which words from each
community's post titles matched.

**[OBSERVE13]** Click the field where the gap between communities is
largest. Look at the sidebar word chips. Are the words that only appear
in one community obviously different in tone or topic from the shared
words? Give a specific example of a word that appears in only one
community and explain what it reveals about that community's concerns.

&nbsp;

&nbsp;

&nbsp;

**[OBSERVE14]** Try two communities you would expect to be semantically
*similar* — for example `r/worldnews` vs `r/news`, or `r/learnpython`
vs `r/programming`. Do their radar polygons look nearly identical, or
do meaningful differences still emerge? Which field shows the most
surprising divergence given how similar the communities seem?

&nbsp;

&nbsp;

**[REFLECT]** The semantic fields are defined by a fixed word list written
by a human. A word like "plant" is in the *Nature* field, but it could
equally appear in a *Work* context (a manufacturing plant) or a *Science*
context (a biology experiment). What does it mean to assign a word to a
single semantic field? How might ambiguous words like this distort the
radar chart, and what would a more sophisticated approach look like?

&nbsp;

&nbsp;

---

*CS 108 — The Art and Practice of Computer Science | Walla Walla University*
