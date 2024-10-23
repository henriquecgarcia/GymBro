from django.db import models
from django.contrib.auth.models import User
# from django.contrib.gis.db import models as gis_models
from django.core.validators import MinValueValidator, MaxValueValidator

# from .models import User

class GymUser(models.Model):
	# Ligação com o modelo User padrão do Django
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	nome = models.CharField(max_length=100)
	idade = models.IntegerField(validators=[MinValueValidator(18)])  # Apenas para maiores de 18 anos
	genero_opcoes = [
		('cis-homem', 'Cis-homem'),
		('cis-mulher', 'Cis-mulher'),
		('trans-homem', 'Trans-homem'),
		('trans-mulher', 'Trans-mulher'),
		('outro', 'Outro'),
	]
	genero = models.CharField(max_length=100, choices=genero_opcoes)
	bio = models.TextField(blank=True)
	avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

	data_cadastro = models.DateTimeField(auto_now_add=True)
	ultimo_login = models.DateTimeField(auto_now=True)

	ultima_loc_lat = models.FloatField(null=True, blank=True)
	ultima_loc_long = models.FloatField(null=True, blank=True)

	avaliacao = models.FloatField(default=5.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

	academia = models.CharField(max_length=100, blank=True)
	premium = models.BooleanField(default=False)

	objetivo_opcoes = [
		('perder_peso', 'Perder Peso'),
		('ganhar_massa', 'Ganhar Massa'),
		('definicao', 'Definição'),
		('saude_geral', 'Saúde Geral'),
		('competicao', 'Competição'),
		('outro', 'Outro'),
	]
	objetivo = models.CharField(max_length=100, choices=objetivo_opcoes, blank=True)

	pontos_acumulados = models.IntegerField(default=0)

	def __str__(self):
		return self.nome

class GymMach(models.Model):
	user1 = models.ForeignKey(GymUser, on_delete=models.CASCADE, related_name='user1')
	user2 = models.ForeignKey(GymUser, on_delete=models.CASCADE, related_name='user2')
	criado_em = models.DateTimeField(auto_now_add=True)
	ultima_mensagem = models.DateTimeField(auto_now=True)

class GymMachMessage(models.Model):
	autor = models.ForeignKey(GymUser, on_delete=models.CASCADE)
	mensagem = models.TextField()
	criado_em = models.DateTimeField(auto_now_add=True)
	mach = models.ForeignKey(GymMach, on_delete=models.CASCADE)
