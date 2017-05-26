# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from crawler.items import CrawlerItem
from scrapy_splash import SplashRequest

class LeetcodeSpider(scrapy.Spider):
    name = 'leetcode'
    allowed_domains = ['leetcode.com']
    start_urls = ['https://leetcode.com/problemset/algorithms/']

    def start_requests(self):
        for url in self.start_urls:
            meta = {
                'splash':{
                    'endpoint' : 'render.html',
                    'args' : {
                        'wait': 0.5,
                        'image' : 0,
                        'render_all' : 1
                    }
                }

            }
            yield scrapy.Request(url, self.parse, meta=meta)

    def parse(self, response):
        sites = ['/problems/two-sum','/problems/add-two-numbers',
                 '/problems/longest-substring-without-repeating-characters','/problems/median-of-two-sorted-arrays',
                 '/problems/longest-palindromic-substring','/problems/zigzag-conversion','/problems/reverse-integer',
                 '/problems/string-to-integer-atoi','/problems/palindrome-number',
                 '/problems/regular-expression-matching','/problems/container-with-most-water',
                 '/problems/integer-to-roman','/problems/roman-to-integer','/problems/longest-common-prefix',
                 '/problems/3sum','/problems/3sum-closest','/problems/letter-combinations-of-a-phone-number',
                 '/problems/4sum','/problems/remove-nth-node-from-end-of-list','/problems/valid-parentheses',
                 '/problems/merge-two-sorted-lists','/problems/generate-parentheses','/problems/merge-k-sorted-lists',
                 '/problems/swap-nodes-in-pairs','/problems/reverse-nodes-in-k-group',
                 '/problems/remove-duplicates-from-sorted-array','/problems/remove-element','/problems/implement-strstr',
                 '/problems/divide-two-integers','/problems/substring-with-concatenation-of-all-words',
                 '/problems/next-permutation','/problems/longest-valid-parentheses','/problems/search-in-rotated-sorted-array',
                 '/problems/search-for-a-range','/problems/search-insert-position','/problems/valid-sudoku',
                 '/problems/sudoku-solver','/problems/count-and-say','/problems/combination-sum',
                 '/problems/combination-sum-ii','/problems/first-missing-positive','/problems/trapping-rain-water',
                 '/problems/multiply-strings','/problems/wildcard-matching','/problems/jump-game-ii',
                 '/problems/permutations','/problems/permutations-ii','/problems/rotate-image','/problems/anagrams',
                 '/problems/powx-n','/problems/n-queens','/problems/n-queens-ii','/problems/maximum-subarray',
                 '/problems/spiral-matrix','/problems/jump-game','/problems/merge-intervals','/problems/insert-interval',
                 '/problems/length-of-last-word','/problems/spiral-matrix-ii','/problems/permutation-sequence',
                 '/problems/rotate-list','/problems/unique-paths','/problems/unique-paths-ii','/problems/minimum-path-sum',
                 '/problems/valid-number','/problems/plus-one','/problems/add-binary','/problems/text-justification',
                 '/problems/sqrtx','/problems/climbing-stairs','/problems/simplify-path','/problems/edit-distance',
                 '/problems/set-matrix-zeroes','/problems/search-a-2d-matrix','/problems/sort-colors',
                 '/problems/minimum-window-substring','/problems/combinations','/problems/subsets',
                 '/problems/word-search','/problems/remove-duplicates-from-sorted-array-ii',
                 '/problems/search-in-rotated-sorted-array-ii','/problems/remove-duplicates-from-sorted-list-ii',
                 '/problems/remove-duplicates-from-sorted-list','/problems/largest-rectangle-in-histogram',
                 '/problems/maximal-rectangle','/problems/partition-list','/problems/scramble-string',
                 '/problems/merge-sorted-array','/problems/gray-code','/problems/subsets-ii','/problems/decode-ways',
                 '/problems/reverse-linked-list-ii','/problems/restore-ip-addresses','/problems/binary-tree-inorder-traversal',
                 '/problems/unique-binary-search-trees-ii','/problems/unique-binary-search-trees',
                 '/problems/interleaving-string','/problems/validate-binary-search-tree',
                 '/problems/recover-binary-search-tree','/problems/same-tree','/problems/symmetric-tree',
                 '/problems/binary-tree-level-order-traversal','/problems/binary-tree-zigzag-level-order-traversal',
                 '/problems/maximum-depth-of-binary-tree',
                 '/problems/construct-binary-tree-from-preorder-and-inorder-traversal',
                 '/problems/construct-binary-tree-from-inorder-and-postorder-traversal',
                 '/problems/binary-tree-level-order-traversal-ii','/problems/convert-sorted-array-to-binary-search-tree',
                 '/problems/convert-sorted-list-to-binary-search-tree','/problems/balanced-binary-tree',
                 '/problems/minimum-depth-of-binary-tree','/problems/path-sum','/problems/path-sum-ii',
                 '/problems/flatten-binary-tree-to-linked-list','/problems/distinct-subsequences',
                 '/problems/populating-next-right-pointers-in-each-node',
                 '/problems/populating-next-right-pointers-in-each-node-ii','/problems/pascals-triangle',
                 '/problems/pascals-triangle-ii','/problems/triangle','/problems/best-time-to-buy-and-sell-stock',
                 '/problems/best-time-to-buy-and-sell-stock-ii','/problems/best-time-to-buy-and-sell-stock-iii',
                 '/problems/binary-tree-maximum-path-sum','/problems/valid-palindrome','/problems/word-ladder-ii',
                 '/problems/word-ladder','/problems/longest-consecutive-sequence','/problems/sum-root-to-leaf-numbers',
                 '/problems/surrounded-regions','/problems/palindrome-partitioning','/problems/palindrome-partitioning-ii',
                 '/problems/clone-graph','/problems/gas-station','/problems/candy','/problems/single-number',
                 '/problems/single-number-ii','/problems/copy-list-with-random-pointer','/problems/word-break',
                 '/problems/word-break-ii','/problems/linked-list-cycle','/problems/linked-list-cycle-ii',
                 '/problems/reorder-list','/problems/binary-tree-preorder-traversal',
                 '/problems/binary-tree-postorder-traversal','/problems/lru-cache','/problems/insertion-sort-list',
                 '/problems/sort-list','/problems/max-points-on-a-line','/problems/evaluate-reverse-polish-notation',
                 '/problems/reverse-words-in-a-string','/problems/maximum-product-subarray',
                 '/problems/find-minimum-in-rotated-sorted-array','/problems/find-minimum-in-rotated-sorted-array-ii',
                 '/problems/min-stack','/problems/binary-tree-upside-down','/problems/read-n-characters-given-read4',
                 '/problems/read-n-characters-given-read4-ii-call-multiple-times',
                 '/problems/longest-substring-with-at-most-two-distinct-characters',
                 '/problems/intersection-of-two-linked-lists','/problems/one-edit-distance','/problems/find-peak-element',
                 '/problems/missing-ranges','/problems/maximum-gap','/problems/compare-version-numbers',
                 '/problems/fraction-to-recurring-decimal','/problems/two-sum-ii-input-array-is-sorted',
                 '/problems/excel-sheet-column-title','/problems/majority-element',
                 '/problems/two-sum-iii-data-structure-design','/problems/excel-sheet-column-number',
                 '/problems/factorial-trailing-zeroes','/problems/binary-search-tree-iterator','/problems/dungeon-game',
                 '/problems/largest-number','/problems/reverse-words-in-a-string-ii','/problems/repeated-dna-sequences',
                 '/problems/best-time-to-buy-and-sell-stock-iv','/problems/rotate-array','/problems/reverse-bits',
                 '/problems/number-of-1-bits','/problems/house-robber','/problems/binary-tree-right-side-view',
                 '/problems/number-of-islands','/problems/bitwise-and-of-numbers-range','/problems/happy-number',
                 '/problems/remove-linked-list-elements','/problems/count-primes','/problems/isomorphic-strings',
                 '/problems/reverse-linked-list','/problems/course-schedule','/problems/implement-trie-prefix-tree',
                 '/problems/minimum-size-subarray-sum','/problems/course-schedule-ii',
                 '/problems/add-and-search-word-data-structure-design','/problems/word-search-ii',
                 '/problems/house-robber-ii','/problems/shortest-palindrome','/problems/kth-largest-element-in-an-array',
                 '/problems/combination-sum-iii','/problems/contains-duplicate','/problems/the-skyline-problem',
                 '/problems/contains-duplicate-ii','/problems/contains-duplicate-iii','/problems/maximal-square',
                 '/problems/count-complete-tree-nodes','/problems/rectangle-area','/problems/basic-calculator',
                 '/problems/implement-stack-using-queues','/problems/invert-binary-tree','/problems/basic-calculator-ii',
                 '/problems/summary-ranges','/problems/majority-element-ii','/problems/kth-smallest-element-in-a-bst',
                 '/problems/power-of-two','/problems/implement-queue-using-stacks','/problems/number-of-digit-one',
                 '/problems/palindrome-linked-list','/problems/lowest-common-ancestor-of-a-binary-search-tree',
                 '/problems/lowest-common-ancestor-of-a-binary-tree','/problems/delete-node-in-a-linked-list',
                 '/problems/product-of-array-except-self','/problems/sliding-window-maximum',
                 '/problems/search-a-2d-matrix-ii','/problems/different-ways-to-add-parentheses',
                 '/problems/valid-anagram','/problems/shortest-word-distance',
                 '/problems/shortest-word-distance-ii','/problems/shortest-word-distance-iii',
                 '/problems/strobogrammatic-number','/problems/strobogrammatic-number-ii',
                 '/problems/strobogrammatic-number-iii','/problems/group-shifted-strings',
                 '/problems/count-univalue-subtrees','/problems/flatten-2d-vector','/problems/meeting-rooms',
                 '/problems/meeting-rooms-ii','/problems/factor-combinations',
                 '/problems/verify-preorder-sequence-in-binary-search-tree','/problems/paint-house',
                 '/problems/binary-tree-paths','/problems/add-digits','/problems/3sum-smaller',
                 '/problems/single-number-iii','/problems/graph-valid-tree','/problems/ugly-number',
                 '/problems/ugly-number-ii','/problems/paint-house-ii','/problems/palindrome-permutation',
                 '/problems/palindrome-permutation-ii','/problems/missing-number','/problems/alien-dictionary',
                 '/problems/closest-binary-search-tree-value','/problems/encode-and-decode-strings',
                 '/problems/closest-binary-search-tree-value-ii','/problems/integer-to-english-words','/problems/h-index',
                 '/problems/h-index-ii','/problems/paint-fence','/problems/find-the-celebrity','/problems/first-bad-version',
                 '/problems/perfect-squares','/problems/wiggle-sort','/problems/zigzag-iterator',
                 '/problems/expression-add-operators','/problems/move-zeroes','/problems/peeking-iterator',
                 '/problems/inorder-successor-in-bst','/problems/walls-and-gates','/problems/find-the-duplicate-number',
                 '/problems/unique-word-abbreviation','/problems/game-of-life','/problems/word-pattern',
                 '/problems/word-pattern-ii','/problems/nim-game','/problems/flip-game','/problems/flip-game-ii',
                 '/problems/find-median-from-data-stream','/problems/best-meeting-point',
                 '/problems/serialize-and-deserialize-binary-tree','/problems/binary-tree-longest-consecutive-sequence',
                 '/problems/bulls-and-cows','/problems/longest-increasing-subsequence',
                 '/problems/remove-invalid-parentheses','/problems/smallest-rectangle-enclosing-black-pixels',
                 '/problems/range-sum-query-immutable','/problems/range-sum-query-2d-immutable','/problems/number-of-islands-ii','/problems/additive-number','/problems/range-sum-query-mutable','/problems/range-sum-query-2d-mutable','/problems/best-time-to-buy-and-sell-stock-with-cooldown','/problems/minimum-height-trees','/problems/sparse-matrix-multiplication','/problems/burst-balloons','/problems/super-ugly-number','/problems/binary-tree-vertical-order-traversal','/problems/count-of-smaller-numbers-after-self','/problems/remove-duplicate-letters','/problems/shortest-distance-from-all-buildings','/problems/maximum-product-of-word-lengths','/problems/bulb-switcher','/problems/generalized-abbreviation','/problems/create-maximum-number','/problems/coin-change','/problems/number-of-connected-components-in-an-undirected-graph','/problems/wiggle-sort-ii','/problems/maximum-size-subarray-sum-equals-k','/problems/power-of-three','/problems/count-of-range-sum','/problems/odd-even-linked-list','/problems/longest-increasing-path-in-a-matrix','/problems/patching-array','/problems/verify-preorder-serialization-of-a-binary-tree','/problems/reconstruct-itinerary','/problems/largest-bst-subtree','/problems/increasing-triplet-subsequence','/problems/self-crossing','/problems/palindrome-pairs','/problems/house-robber-iii','/problems/counting-bits','/problems/nested-list-weight-sum','/problems/longest-substring-with-at-most-k-distinct-characters','/problems/flatten-nested-list-iterator','/problems/power-of-four','/problems/integer-break','/problems/reverse-string','/problems/reverse-vowels-of-a-string','/problems/moving-average-from-data-stream','/problems/top-k-frequent-elements','/problems/design-tic-tac-toe','/problems/intersection-of-two-arrays','/problems/intersection-of-two-arrays-ii','/problems/android-unlock-patterns','/problems/data-stream-as-disjoint-intervals','/problems/design-snake-game','/problems/russian-doll-envelopes','/problems/design-twitter','/problems/line-reflection','/problems/count-numbers-with-unique-digits','/problems/rearrange-string-k-distance-apart','/problems/logger-rate-limiter','/problems/sort-transformed-array','/problems/bomb-enemy','/problems/design-hit-counter','/problems/max-sum-of-sub-matrix-no-larger-than-k','/problems/nested-list-weight-sum-ii','/problems/water-and-jug-problem','/problems/find-leaves-of-binary-tree','/problems/valid-perfect-square','/problems/largest-divisible-subset','/problems/plus-one-linked-list','/problems/range-addition','/problems/sum-of-two-integers','/problems/super-pow','/problems/find-k-pairs-with-smallest-sums','/problems/guess-number-higher-or-lower','/problems/guess-number-higher-or-lower-ii','/problems/wiggle-subsequence','/problems/combination-sum-iv','/problems/kth-smallest-element-in-a-sorted-matrix','/problems/design-phone-directory','/problems/insert-delete-getrandom-o1','/problems/insert-delete-getrandom-o1-duplicates-allowed','/problems/linked-list-random-node','/problems/ransom-note','/problems/shuffle-an-array','/problems/mini-parser','/problems/lexicographical-numbers','/problems/first-unique-character-in-a-string','/problems/longest-absolute-file-path','/problems/find-the-difference','/problems/elimination-game','/problems/perfect-rectangle','/problems/is-subsequence','/problems/utf-8-validation','/problems/decode-string','/problems/longest-substring-with-at-least-k-repeating-characters','/problems/rotate-function','/problems/integer-replacement','/problems/random-pick-index','/problems/evaluate-division','/problems/nth-digit','/problems/binary-watch','/problems/remove-k-digits','/problems/frog-jump','/problems/sum-of-left-leaves','/problems/convert-a-number-to-hexadecimal','/problems/queue-reconstruction-by-height','/problems/trapping-rain-water-ii','/problems/valid-word-abbreviation','/problems/longest-palindrome','/problems/split-array-largest-sum','/problems/minimum-unique-word-abbreviation','/problems/fizz-buzz','/problems/arithmetic-slices','/problems/third-maximum-number','/problems/add-strings','/problems/partition-equal-subset-sum','/problems/pacific-atlantic-water-flow','/problems/sentence-screen-fitting','/problems/battleships-in-a-board','/problems/strong-password-checker','/problems/maximum-xor-of-two-numbers-in-an-array','/problems/valid-word-square','/problems/reconstruct-original-digits-from-english','/problems/longest-repeating-character-replacement','/problems/word-squares','/problems/all-oone-data-structure','/problems/number-of-segments-in-a-string','/problems/non-overlapping-intervals','/problems/find-right-interval','/problems/path-sum-iii','/problems/find-all-anagrams-in-a-string','/problems/ternary-expression-parser','/problems/k-th-smallest-in-lexicographical-order','/problems/arranging-coins','/problems/find-all-duplicates-in-an-array','/problems/sequence-reconstruction','/problems/add-two-numbers-ii','/problems/arithmetic-slices-ii-subsequence','/problems/number-of-boomerangs','/problems/find-all-numbers-disappeared-in-an-array','/problems/serialize-and-deserialize-bst','/problems/delete-node-in-a-bst','/problems/sort-characters-by-frequency','/problems/minimum-number-of-arrows-to-burst-balloons','/problems/minimum-moves-to-equal-array-elements','/problems/4sum-ii','/problems/assign-cookies','/problems/132-pattern','/problems/repeated-substring-pattern','/problems/lfu-cache','/problems/hamming-distance','/problems/minimum-moves-to-equal-array-elements-ii','/problems/island-perimeter','/problems/can-i-win','/problems/optimal-account-balancing','/problems/count-the-repetitions','/problems/unique-substrings-in-wraparound-string','/problems/validate-ip-address','/problems/convex-polygon','/problems/encode-string-with-shortest-length','/problems/concatenated-words','/problems/matchsticks-to-square','/problems/ones-and-zeroes','/problems/heaters','/problems/number-complement','/problems/total-hamming-distance','/problems/sliding-window-median','/problems/magical-string','/problems/license-key-formatting','/problems/smallest-good-base','/problems/find-permutation','/problems/max-consecutive-ones','/problems/predict-the-winner','/problems/max-consecutive-ones-ii','/problems/zuma-game','/problems/the-maze','/problems/increasing-subsequences','/problems/construct-the-rectangle','/problems/reverse-pairs','/problems/target-sum','/problems/teemo-attacking','/problems/next-greater-element-i','/problems/diagonal-traverse','/problems/the-maze-iii','/problems/keyboard-row','/problems/find-mode-in-binary-search-tree','/problems/ipo','/problems/next-greater-element-ii','/problems/base-7','/problems/the-maze-ii','/problems/relative-ranks','/problems/perfect-number','/problems/most-frequent-subtree-sum','/problems/find-bottom-left-tree-value','/problems/freedom-trail','/problems/find-largest-value-in-each-tree-row','/problems/longest-palindromic-subsequence','/problems/super-washing-machines','/problems/detect-capital','/problems/longest-uncommon-subsequence-i','/problems/longest-uncommon-subsequence-ii','/problems/continuous-subarray-sum','/problems/longest-word-in-dictionary-through-deleting','/problems/contiguous-array','/problems/beautiful-arrangement','/problems/word-abbreviation','/problems/minesweeper','/problems/minimum-absolute-difference-in-bst','/problems/lonely-pixel-i','/problems/k-diff-pairs-in-an-array','/problems/lonely-pixel-ii','/problems/encode-and-decode-tinyurl','/problems/construct-binary-tree-from-string','/problems/complex-number-multiplication','/problems/convert-bst-to-greater-tree','/problems/minimum-time-difference','/problems/reverse-string-ii','/problems/01-matrix','/problems/diameter-of-binary-tree','/problems/output-contest-matches','/problems/boundary-of-binary-tree','/problems/remove-boxes','/problems/friend-circles','/problems/split-array-with-equal-sum','/problems/binary-tree-longest-consecutive-sequence-ii','/problems/student-attendance-record-i','/problems/student-attendance-record-ii','/problems/optimal-division','/problems/brick-wall','/problems/split-concatenated-strings','/problems/next-greater-element-iii','/problems/reverse-words-in-a-string-iii','/problems/subarray-sum-equals-k','/problems/array-partition-i','/problems/longest-line-of-consecutive-one-in-matrix','/problems/binary-tree-tilt','/problems/find-the-closest-palindrome','/problems/reshape-the-matrix','/problems/permutation-in-string','/problems/maximum-vacation-days','/problems/subtree-of-another-tree','/problems/squirrel-simulation','/problems/distribute-candies','/problems/out-of-boundary-paths','/problems/shortest-unsorted-continuous-subarray','/problems/kill-process','/problems/delete-operation-for-two-strings','/problems/erect-the-fence','/problems/design-in-memory-file-system','/problems/fraction-addition-and-subtraction','/problems/valid-square','/problems/longest-harmonious-subsequence',]
        for site in sites:
            url = "https://leetcode.com" + site
            item = CrawlerItem()
            item['link'] = url
            yield Request(url=url, meta={'item': item}, callback=self.parse_item)

    def parse_item(self, response):
        item = response.meta['item']
        item['title'] = Selector(response).xpath('//title/text()').extract()[0]
        item['content'] = ''.join(Selector(response).xpath('//div[@class="question-content"]/node()').extract())
        item['tag'] = Selector(response).xpath('//*[@id="descriptionContent"]/div[1]/div[2]/div[2]/span').extract()
        item['similarProblem'] = Selector(response).xpath('//*[@id="descriptionContent"]/div[1]/div[2]/div[3]/span').extract()
        return item
