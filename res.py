# Resource variables for the bot

## Catagories of Hedonism ##
# Luxury
luxury_keywords = ('guchi', 'expensive', 'decadent',
                   'gourgious', 'gold', 'gems', 'spice', )
luxury_quotes = ('It seems {} hates humans the way I hate having my nipples polished with industrial sand paper.',
                 'Nothing but the most expensive and decadent scented towels would satisfy {} tastes. How wonderful!',
                 'I have no use for it anymore {}, it has done everyone and everything.')


# Sex
sex_keywords = ('sex', 'orgy', 'laid', 'lust', 'hot',
                'sordid', 'unconventional love', 'threesome', 'hedonist', 'hedonistic')
sex_quotes = ('Hello, {}. Might I procure your services? Oh, nothing sordid, I assure you! Simply vomit on me, ever so gently, while I humiliate a pheasant.',
              'I too have known unconventional love. Perhaps {} and I... and Djambi, can get together and compare notes sometime.',
              'Ooooooo! Room for one more {}? ',
              'I trust the orgy pit has been scraped and buttered {}!')

# Gluttony
gluttony_keywords = ('stuffed', 'good food', 'feast',
                     'gorge', 'starving', 'chocolate', 'grapes')
gluttony_quotes = ('And just when I was beginning to lose interest {}... Djambi, the chocolate icing!',
                   'One can never have too many candied nuts! Isn\'t that right {}?',
                   'Let the wine flow like the tears of one-thousand boiled geese {}!')


# Relaxation
relaxation_keywords = ('nap', 'lounge', 'hang out',
                       'lay down', 'relax', 'relaxation', 'relaxing')
relaxation_quotes = ('Let us cavort like the Greeks of old! You know the ones I mean {} :)',
                     'There\'s no debauchery like end-of-the-world-debauchery! {}\'s lips, my lips, apocalypse, oo-whoo!')

# Entertainment
entertainment_keywords = ('party', 'rager', 'play',
                          'movie', 'attention', 'interest', 'awesome', 'cool', 'rad')
entertainment_quotes = ('Let the games begin {}!',
                        'And just when I was beginning to lose interest {}... Djambi, the chocolate icing!')


# Vanity
vanity_keywords = ('my picture', 'my face', 'gourgious selfie',
                   'beautiful selfie', 'hot selfie', 'look at me')
vanity_quotes = ('{}\'s latest performance was as delectable as dipping my bottom over and over into a bath of the silkiest oils and creams.',
                 'I appologize for nothing {}!',
                 '{}\'s face is more scrumptious than Djambi\'s finest brasserie!',
                 'And just when I was beginning to lose interest {}... Djambi, the chocolate icing!')

# Lookup dictionary
look = {luxury_keywords: luxury_quotes, sex_keywords: sex_quotes, gluttony_keywords: gluttony_quotes,
        relaxation_keywords: relaxation_quotes, entertainment_keywords: entertainment_quotes, vanity_keywords: vanity_quotes}

# Summoning charm
summon = '!hedbot'

# Post timer. Limit automatic responses to once in this period.
min_break = 600 #s in one hour