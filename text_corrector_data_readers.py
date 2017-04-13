from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random

from data_reader import DataReader, PAD_TOKEN, EOS_TOKEN, GO_TOKEN


class PTBDataReader(DataReader):
    """
    DataReader used to read in the Penn Treebank dataset.
    """

    UNKNOWN_TOKEN = "<unk>"  # already defined in the source data

    DROPOUT_WORDS = {"a", "an", "the"}
    DROPOUT_PROB = 0.25

    REPLACEMENTS = {"there": "their", "their": "there"}
    REPLACEMENT_PROB = 0.25

    def __init__(self, config, train_path):
        super(PTBDataReader, self).__init__(
            config, train_path, special_tokens=[PAD_TOKEN, GO_TOKEN, EOS_TOKEN])

        self.UNKNOWN_ID = self.token_to_id[PTBDataReader.UNKNOWN_TOKEN]

    def read_samples_by_string(self, path):

        for line in self.read_tokens(path):
            source = []
            target = []

            for token in line:
                target.append(token)

                # Randomly dropout some words from the input.
                dropout_word = (token in PTBDataReader.DROPOUT_WORDS and
                                random.random() < PTBDataReader.DROPOUT_PROB)
                replace_word = (token in PTBDataReader.REPLACEMENTS and
                                random.random() <
                                PTBDataReader.REPLACEMENT_PROB)

                if replace_word:
                    source.append(PTBDataReader.REPLACEMENTS[token])
                elif not dropout_word:
                    source.append(token)

            yield source, target

    def unknown_token(self):
        return PTBDataReader.UNKNOWN_TOKEN

    def read_tokens(self, path):
        with open(path, "r") as f:
            for line in f:
                yield line.rstrip().lstrip().split()


class MovieDialogReader(DataReader):
    """
    DataReader used to read and tokenize data from the Cornell open movie
    dialog dataset.
    """

    UNKNOWN_TOKEN = "UNK"

    DROPOUT_TOKENS = {"a", "an", "the", "'ll", "'s", "'m", "'ve"}  # Add "to"

    REPLACEMENTS = {"there": "their", "their": "there", "then": "than",
                    "than": "then"}
    # Add: "be":"to"

    def __init__(self, config, train_path=None, token_to_id=None,
                 dropout_prob=0.25, replacement_prob=0.25, dataset_copies=2):
        super(MovieDialogReader, self).__init__(
            config, train_path=train_path, token_to_id=token_to_id,
            special_tokens=[
                PAD_TOKEN, GO_TOKEN, EOS_TOKEN,
                MovieDialogReader.UNKNOWN_TOKEN],
            dataset_copies=dataset_copies)

        self.dropout_prob = dropout_prob
        self.replacement_prob = replacement_prob

        self.UNKNOWN_ID = self.token_to_id[MovieDialogReader.UNKNOWN_TOKEN]

    def read_samples_by_string(self, path):
        for tokens in self.read_tokens(path):
            source = []
            target = []

            for token in tokens:
                target.append(token)

                # Randomly dropout some words from the input.
                dropout_token = (token in MovieDialogReader.DROPOUT_TOKENS and
                                random.random() < self.dropout_prob)
                replace_token = (token in MovieDialogReader.REPLACEMENTS and
                                random.random() < self.replacement_prob)

                if replace_token:
                    source.append(MovieDialogReader.REPLACEMENTS[token])
                elif not dropout_token:
                    source.append(token)

            yield source, target

    def unknown_token(self):
        return MovieDialogReader.UNKNOWN_TOKEN

    def read_tokens(self, path):
        with open(path, "r") as f:
            for line in f:
                yield line.lower().strip().split()

class FCEReader(DataReader):
    """
    DataReader used to read and tokenize data from the FCE dataset.
    """

    UNKNOWN_TOKEN = "UNK"

    DROPOUT_TOKENS = {"a", "an", "the", "'ll", "'s", "'m", "'ve"}  # Add "to"

    REPLACEMENTS = {"there": "their", "their": "there", "then": "than",
                    "than": "then"}
    # Add: "be":"to"

    def __init__(self, config, train_path=None, token_to_id=None,
                 dropout_prob=0.25, replacement_prob=0.25, dataset_copies=2):
        super(FCEReader, self).__init__(
            config, train_path=train_path, token_to_id=token_to_id,
            special_tokens=[
                PAD_TOKEN, GO_TOKEN, EOS_TOKEN,
                FCEReader.UNKNOWN_TOKEN],
            dataset_copies=dataset_copies)

        self.dropout_prob = dropout_prob
        self.replacement_prob = replacement_prob

        self.UNKNOWN_ID = self.token_to_id[FCEReader.UNKNOWN_TOKEN]

    def read_samples_by_string(self, path):
        with open(path, "r") as f:
            while True:
                line1 = f.readline()
                if not line1:
                    break
                line2 = f.readline()
                if not line2:
                    break
                source = line1.lower()[5:].strip().split()
                target = line2.lower()[5:].strip().split()
                yield source, target

    def unknown_token(self):
        return FCEReader.UNKNOWN_TOKEN

    def read_tokens(self, path):
        i = 0
        with open(path, "r") as f:
            for line in f:
                if i%2 == 1:
                    yield line.lower()[5:].strip().split()
                i+=1