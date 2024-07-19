# Omnipedia

Scaling production, evalution, and refinement of frontier knowledge since MMXXIIII.

![](omnipedia.jpeg)

The omnipedia is a wiki for frontier knowledge which uses a mix of LLM (such as [storm](https://github.com/stanford-oval/storm/)) and editor input to create *just-in-time* articles in response to searches. Articles in omnipedia include incomplete, obscure, and unverified summaries of topics not covered by more reliable reference works. These are clustered and improved over time. To minimize the risk of confusion with reliable sources, omnipedia articles have colored backdrops.

- **Red:** newly AI generated pages start in the red category indicating that they should be targeted for editing, rather than for reading.
- **Red-to-Yellow:** Red pages are periodically evaluated by a battery of classifiers targeting various requirement derived from the wikipedia style guides. Articles that pass the automated tests are recategorized as yellow.
- **Yellow:** Yellow pages passes the letter of the rules for wikipedia articles but they may not pass the spirit of rules. Use with caution. Editors should focus on detecting and revising gaps between the letter and the spirit of the guidelines.
- **Yellow-to-Green:** Yellow pages are periodically evaluated by human moderators who manually verify whether the article does in fact satisfy the requirements. Once a moderator is satisfied that the requirements are met they can transition its color.
- **Green:** Green articles are vetted frontier knowledge, approaching the boundary of (but not necessarily satisfying) the criteria for wikipedia inclusion. Users are encourage to treat green articles as emerging knowledge.
- **Green-to-White:** Omnipedia has no say in whether green articles get included in wikipedia but the Omnipedia system is designed to facilitate transfer of control of its pages to wikipedia should wikipedia moderators deem that transfer desirable.

## Technical Approach

Omnipedia is BOTH a fork and a mirror of wikipedia

- Mirroring or transcluding canonical content and treating it as canonical (defering to wikipedia editorial process and governance of canonical content)
- [Forking]([url](https://en.wikipedia.org/wiki/Wikipedia:FAQ/Forking)) the software and social protocols to support frontier knowledge (retaining compatitability so that edit histories and other article provenance are legible/interoperable with wikipedia)
