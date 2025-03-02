import torch

print(torch.cuda.is_available())  # Deve retornar True se estiver funcionando
print(torch.cuda.device_count())  # Deve mostrar o número de GPUs disponíveis
print(torch.cuda.get_device_name(0))  # Nome da GPU AMD