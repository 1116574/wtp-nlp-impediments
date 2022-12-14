import logging

from wtp_nlp.nlp.highlihter import tokenizer
from wtp_nlp.nlp.compound_tokens import execute

from wtp_nlp.data.patterns import get_patterns
from wtp_nlp.data.tokens import Dummy


def language_processor(text):
    logger = logging.getLogger('nlp')
    results = []
    token_collection = tokenizer(text)

    # Remove 0-delimitered duplicate tokens
    for i, tok in enumerate(token_collection):
        if tok == 0:
            try:
                prev = token_collection[i-1]
                next = token_collection[i+1]
                if prev == next or type(prev) == type(next):
                    logger.warning(f'Token duplication removed. This shouldnt happen anymore. {token_collection}')
                    token_collection[i] = Dummy
                    token_collection[i+1] = Dummy
            except IndexError:
                pass

    while Dummy in token_collection:
        token_collection.remove(Dummy)

    logger.debug(f'tokenizer returned: {token_collection}')

    # Find patterns & get their results
    patterns = get_patterns()
    for pattern_name, matching_text, final in execute(token_collection, patterns):
        results.append({
            'name': pattern_name,
            'matched': matching_text,
            'processed_to': final
        })
    pass

    return results