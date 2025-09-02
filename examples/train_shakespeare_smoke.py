# config/train_shakespeare_smoke.py
# Minimal config for quick NanoGPT testing on Shakespeare
# Runs on GPU with 8GB VRAM, completes in a couple of minutes

out_dir = 'out-shakespeare-smoke'
eval_interval = 20
eval_iters = 20
log_interval = 10
always_save_checkpoint = False

wandb_log = False
wandb_project = 'shakespeare-char'
wandb_run_name = 'smoke-gpt'

dataset = 'shakespeare_char'
gradient_accumulation_steps = 1
batch_size = 32
block_size = 128

n_layer = 4
n_head = 4
n_embd = 192
dropout = 0.0

learning_rate = 1e-3
max_iters = 200
lr_decay_iters = 200
min_lr = 1e-4
beta2 = 0.99
warmup_iters = 10

device = 'cuda'
compile = False
