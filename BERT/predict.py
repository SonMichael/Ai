
from library import *
from data import Dataset
from bert.model import Bert
from trainer import Trainer
from bert.optimizer import CustomLearningRate
import logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    parser = ArgumentParser()
    home_dir = os.getcwd()
    parser.add_argument("--checkpoint-folder", default='{}/checkpoints/'.format(home_dir), type=str)
    parser.add_argument("--epochs", default=10, type=int)
    args = parser.parse_args()
    n_layers = 6 # number of Encoder of Encoder Layer
    n_heads = 12 # number of heads in Multi-Head Attention
    d_model = 768 # Embedding Size
    d_ff = 768 * 4  # 4*d_model, FeedForward dimension
    d_k = d_v = 64  # dimension of K(=Q), V
    n_segments = 2
    dropout_rate = 0.1
    eps = 0.1
    epochs = args.epochs
    batch_size = 6
    maxlen = 30
    max_pred = 5
    checkpoint_folder = args.checkpoint_folder
    # FIXME
    dataset = Dataset(batch_size, maxlen, max_pred)
    train_dataset = dataset.build_test_dataset()
    vocab_size = dataset.vocab_size + 1
    bert = Bert(n_layers,n_heads,vocab_size,maxlen,n_segments,d_model,d_ff,dropout_rate,eps)
    lrate = CustomLearningRate(d_model)
    optimizer = tf.keras.optimizers.Adam(lrate, beta_1=0.9, beta_2=0.98, epsilon=1e-9)
    trainer = Trainer(bert, optimizer, epochs, checkpoint_folder)
    number_dict = dataset.number_dict
    trainer.predict(train_dataset, dataset.text, number_dict)



