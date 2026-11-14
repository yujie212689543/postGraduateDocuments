## Slide 1 — Title

Good morning. We are Group 36. Our project studies sequential knowledge editing in GPT-2 XL. We ask: after a new fact is inserted, does it survive many later edits? We compare ROME, MEMIT, and AlphaEdit.

## Slide 2 — Motivation

Here is a controlled edit. The model says Tonga is in Oceania, and we rewrite the answer to North America. A good edit returns the new answer, works on a paraphrase, and leaves unrelated facts unchanged.

Real edits arrive sequentially, and prior work shows ROME and MEMIT can forget earlier changes. So we test whether edits last and whether the ranking holds at scale.

## Slide 3 — Methods

All three methods treat a feed-forward layer as key-value memory. ROME uses a rank-one update in one layer. MEMIT edits five layers and adds a penalty to protect old facts. AlphaEdit keeps the same layers, but replaces the penalty with a null-space projection. With everything else shared, we can isolate the update rule.

## Slide 4 — Edit, score, then score again

We check every fact two times. First, we add facts one by one and check right away if the edit worked. Then, after all 100 edits, we test them again to see if they are still there. We use the GPT-2 XL model and the ZsRE dataset.

## Slide 5 — AlphaEdit keeps the most; MEMIT disturbs the least

Here are the results after 100 edits. AlphaEdit is the best, keeping 97.7% of new answers. ROME keeps 94.5%. MEMIT is the lowest at 84.3%.

Why? At edit time, ROME and AlphaEdit write almost every edit successfully. But MEMIT only writes 83.8%. So, MEMIT fails early. ROME writes successfully, but forgets later. Also, look at the left chart: MEMIT has the best locality, meaning it changes the fewest unrelated facts.

## Slide 6 — The methods fail at different stages

The numbers on the screen show different failure stages. ROME lost 16 edits after writing them. AlphaEdit lost only 2. But MEMIT never wrote 28 edits correctly in the first place. Importantly, ROME and AlphaEdit can edit all these 28 facts perfectly. So, the problem is the MEMIT method itself, not the facts.

## Slide 7 — Ablation

The ablation changes only the update formula. MEMIT, with its penalty, keeps 84.3%. If we remove the penalty, the model collapses: rewrite accuracy falls to 0.1%. Adding AlphaEdit's null-space projection brings it back to 95.3%, and the previous-edit term raises it to 97.7%. So the penalty keeps MEMIT stable but holds back new facts. The projection gives stability without that cost.

## Slide 8 — Scale

At 1,000 edits the picture changes. ROME holds up to about 250 edits, then drops to 50%, because it forgets its early edits. MEMIT ends at 61%, and AlphaEdit stays above 90%. In the paper's setting, with 100 edits per step, our ranking, from lowest to highest, is ROME, MEMIT, AlphaEdit, the same as published. With only 100 edits ROME was ahead of MEMIT, so that difference comes from the number of edits.

## Slide 9 — Conclusion

To conclude: measure twice, once right after an edit and once after all the later edits. ROME and MEMIT fail at different stages, and one final score hides that. AlphaEdit's projection gives stability without MEMIT's cost. Locality and reasoning remain unsolved for all three methods. Thank you.
