# Copyright 2018 The Texar Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Downloads data.
"""
import tensorflow as tf
import texar.tf as tx

# pylint: disable=invalid-name

flags = tf.flags

flags.DEFINE_string("data", "iwslt14", "Data to download [iwslt14|toy_copy]")

FLAGS = flags.FLAGS


def prepare_data():
    """Downloads data.
    """
    if FLAGS.data == 'giga':
        tx.data.maybe_download(
            urls='https://drive.google.com/file/d/'
                 '12RZs7QFwjj6dfuYNQ_0Ah-ccH1xFDMD5/view?usp=sharing',
            path='./',
            filenames='giga.zip',
            extract=True)
    elif FLAGS.data == 'iwslt14':
        tx.data.maybe_download(
            urls='https://drive.google.com/file/d/'
                 '1y4mUWXRS2KstgHopCS9koZ42ENOh6Yb9/view?usp=sharing',
            path='./',
            filenames='iwslt14.zip',
            extract=True)
    else:
        raise ValueError('Unknown data: {}'.format(FLAGS.data))


def main():
    """Entrypoint.
    """
    prepare_data()


if __name__ == '__main__':
    main()
