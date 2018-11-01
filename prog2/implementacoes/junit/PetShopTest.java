import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class PetShopTest {
	
	private PetShop petShop;
	
	@BeforeEach
	public void setUp() {
		petShop = new PetShop();
	}
	
	// testes para os casos em que alguma exceção será lançada.

	@Test
	public void testCadastrarAnimalNomeInvalido() {
		assertThrows(IllegalArgumentException.class, 
				() -> petShop.cadastrarAnimal(null, "Gato", 10));
		
		assertThrows(IllegalArgumentException.class, 
				() -> petShop.cadastrarAnimal("", "Gato", 10));
		
		assertThrows(IllegalArgumentException.class, 
				() -> petShop.cadastrarAnimal("    ", "Gato", 10));
	}
	
	@Test
	public void testCadastrarAnimalEspecieInvalida() {
		assertThrows(IllegalArgumentException.class, 
				() -> petShop.cadastrarAnimal("Julieta", null, 10));
		
		assertThrows(IllegalArgumentException.class, 
				() -> petShop.cadastrarAnimal("Julieta", "", 10));
		
		assertThrows(IllegalArgumentException.class, 
				() -> petShop.cadastrarAnimal("Julieta", "   ", 10));
	}
	
	@Test
	public void testCadastrarAnimalIdadeInvalida() {
		assertThrows(IllegalArgumentException.class, 
				() -> petShop.cadastrarAnimal("Julieta", "Gato", -1));
	}
	
	// testes para casos válidos.
	
	@Test
	public void testCadastrarAnimalValido() {
		assertTrue(petShop.cadastrarAnimal("Julieta", "Gato", 8));
		assertFalse(petShop.cadastrarAnimal("Julieta", "Cachorro", 10));
	}

	@Test
	public void testAnimalExiste() {
		assertFalse(petShop.animalExiste("Aderbaldo"));
		petShop.cadastrarAnimal("Aderbaldo", "Gato", 8);
		assertTrue(petShop.animalExiste("Aderbaldo"));
		assertTrue(petShop.animalExiste("AdErBaLdO"));
	}

	@Test
	public void testMediaIdade() {
		assertEquals(0, petShop.mediaIdade(), 0.01);
		petShop.cadastrarAnimal("Aderbaldo", "Gato", 8);
		petShop.cadastrarAnimal("Aderbaldo", "Sapo", 5); // não deve cadastrar, pois já existe.
		assertEquals(8, petShop.mediaIdade(), 0.0001);
		petShop.cadastrarAnimal("Julieta", "Cachorro", 3);
		petShop.cadastrarAnimal("Garfield", "Gato", 5);
		assertEquals(5.3, petShop.mediaIdade(), 0.04);
	}

	@Test
	public void testTotalAnimaisCadastrados() {
		assertEquals(0, petShop.totalAnimaisCadastrados());
		petShop.cadastrarAnimal("Aderbaldo", "Gato", 8);
		assertEquals(1, petShop.totalAnimaisCadastrados());
		petShop.cadastrarAnimal("Aderbaldo", "Gato", 3);
		assertEquals(1, petShop.totalAnimaisCadastrados());
	}

}