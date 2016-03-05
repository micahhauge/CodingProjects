#include <stdio.h>
#include <string.h>

char cards[15] = {'a', '2', '3', '4', '5', '6', '7',
					  '8', '9', '0', 'j', 'q', 'k'};

int numOfPlayers;
int player;
char myCards[100];
char lc;			//loop controler
char buffer;
int turn = 0;

void clear (void)
{    
  while ( getchar() != '\n' );
}



int cardCount()
{
	int cc;
	int i = 0;
	do
	{
		buffer = myCards[i];
		if(buffer == 'a' || buffer == '2' || buffer == '3' || buffer == '4' || buffer == '5' || buffer == '6' || buffer == '7' || buffer == '8' || buffer == '9' || buffer == '0' || buffer == 'j' || buffer == 'q' || buffer == 'k')
		{
			cc++;
		}

		i++;
	}while(buffer != 'd');

	return cc;

}

void turnPlus()
{
	turn++;
	printf("Turn: %i\n", turn);
}

int cardToNum(char c)
{
	if (c == 'a')
	{
		return 1;
	}
	else if (c == 'j')
	{
		return 11;
	}
	else if (c == 'q')
	{
		return 12;
	}
	else if (c == 'k')
	{
		return 13;
	}

	return 12;
}

char numToCard(int num)
{
	if (num == 1)
	{
		return 'a';
	}
	else if (num == 11)
	{
		return 'j';
	}
	else if (num == 12)
	{
		return 'q';
	}
	else if (num == 13)
	{
		return 'k';
	}
	else if (num == 2)
	{
		return '2';
	}
	else if (num == 3)
	{
		return '3';
	}
	else if (num == 4)
	{
		return '4';
	}
	else if (num == 5)
	{
		return '5';
	}
	else if (num == 6)
	{
		return '6';
	}
	else if (num == 7)
	{
		return '7';
	}
	else if (num == 8)
	{
		return '8';
	}
	else if (num == 9)
	{
		return '9';
	}
	else if (num == 10)
	{
		return '0';
	}
	else
	{
		return 0;
	}
	
}

void printCards()
{
	//clear();
	printf("Your hand:\n");
	int i = 0;
	do
	{
		buffer = myCards[i];
		if(buffer == 'a' || buffer == '2' || buffer == '3' || buffer == '4' || buffer == '5' || buffer == '6' || buffer == '7' || buffer == '8' || buffer == '9' || buffer == '0' || buffer == 'j' || buffer == 'q' || buffer == 'k')
		{
			printf("%c ", buffer);
		}

		i++;
	}while(buffer != 'd');

	printf("\n");



}

void order()
{
	//printCards();
	int cc;
	int i = 0;
	do
	{
		buffer = myCards[i];
		if(buffer == 'a' || buffer == '2' || buffer == '3' || buffer == '4' || buffer == '5' || buffer == '6' || buffer == '7' || buffer == '8' || buffer == '9' || buffer == '0' || buffer == 'j' || buffer == 'q' || buffer == 'k')
		{
			cc++;
		}

		i++;
	}while(buffer != 'd');


	printf("Play cards in this order:\n");
	//printf("cc:%i\nnumP:%i\n", cc, numOfPlayers);

	char wantedList[15];
	int wantedCounter = 0;
	

	int nextCard = player + (turn * numOfPlayers);
	int wanted = 1;

	//printf("%c ", numToCard(nextCard));

	for(int i = 0; i < 13; i++)
	{
		wanted = 1;
		

		for (int j = 0; j < 100; j++)
		{
			//printf("%c", numToCard(nextCard));
			if(myCards[j] == numToCard(nextCard))
			{
				printf("%c ", myCards[j]);
				wanted = 0;
			}
		}

		if (wanted == 1)
		{
			wantedList[wantedCounter] = numToCard(nextCard);
			wantedCounter++;
		}



		nextCard = nextCard + numOfPlayers;
		if (nextCard > 13)
		{
			nextCard = nextCard - 13;
		}

		//printf("%c ", numToCard(nextCard));
		//printf("%i ", nextCard);
	}

	wantedCounter++;
	wantedList[wantedCounter] = 'd';


	printf("\nWanted Order:\n ");
	i = 0;
	do
	{
		buffer = wantedList[i];
		if (buffer != 'd')
		{
			printf("%c ", wantedList[i]);
		}
		i++;
	}while(buffer!='d');

	printf("\n");

}



void removeCards()
{
	//clear();
	if (feof(stdin))
	{
		printCards();
		printf("Enter the cards to remove: ");

		do
		{
			//scanf("%c", &buffer);
			buffer = getchar();
			if(buffer == 'a' || buffer == '2' || buffer == '3' || buffer == '4' || buffer == '5' || buffer == '6' || buffer == '7' || buffer == '8' || buffer == '9' || buffer == '0' || buffer == 'j' || buffer == 'q' || buffer == 'k')
			{
				for (int i = 0; i < 52; i++)
				{
					if (myCards[i] == buffer)
					{
						myCards[i] = 32;
						buffer = 32;
					}
				}
			}
		}while(buffer != '\n');
	}
	else
	{
		do
		{
			//scanf("%c", &buffer);
			buffer = getchar();
			if(buffer == 'a' || buffer == '2' || buffer == '3' || buffer == '4' || buffer == '5' || buffer == '6' || buffer == '7' || buffer == '8' || buffer == '9' || buffer == '0' || buffer == 'j' || buffer == 'q' || buffer == 'k')
			{
				for (int i = 0; i < 52; i++)
				{
					if (myCards[i] == buffer)
					{
						myCards[i] = 32;
						buffer = 32;
					}
				}
			}
		}while(buffer != '\n');
	}
}

void addCards()
{
	clear();

	int i;
	for (i = 0; myCards[i] != 'd'; i++)
	{
		//increment
	}

	printf("Enter the cards to add: ");

	/*
	//printf("\n%i\n", i);
	buffer = getchar();
	while (buffer != '\n')
	{
		//printf("test");
		if(buffer == 'a' || buffer == '2' || buffer == '3' || buffer == '4' || buffer == '5' || buffer == '6' || buffer == '7' || buffer == '8' || buffer == '9' || buffer == '0' || buffer == 'j' || buffer == 'q' || buffer == 'k')
		{
			myCards[i] = buffer;
			i++;
		}
		buffer = getchar();
		//scanf("%c", &buffer);
	}
	myCards[i] = 'd';
	*/

	do
	{
		scanf("%c", &buffer);
		if(buffer == 'a' || buffer == '2' || buffer == '3' || buffer == '4' || buffer == '5' || buffer == '6' || buffer == '7' || buffer == '8' || buffer == '9' || buffer == '0' || buffer == 'j' || buffer == 'q' || buffer == 'k' || buffer == 'd' )
		{
			myCards[i] = buffer;
			i++;
		}
	}while(buffer != 'd');
	

}

int main()
{

	printf("Enter the number of players: ");
	scanf("%i", &numOfPlayers);

	

	printf("Enter your starting cards: ");

	int i = 0;
	//buffer = getchar();
	//scanf("%c", &buffer);
	clear();
	buffer = getchar();
	while (buffer != '\n')
	{
		//printf("test");
		if(buffer == 'a' || buffer == '2' || buffer == '3' || buffer == '4' || buffer == '5' || buffer == '6' || buffer == '7' || buffer == '8' || buffer == '9' || buffer == '0' || buffer == 'j' || buffer == 'q' || buffer == 'k' || buffer == 'd' )
		{
			myCards[i] = buffer;
			i++;
		}
		buffer = getchar();
		//scanf("%c", &buffer);
	}
	myCards[i] = 'd';
	/*
	do
	{
		scanf("%c", &buffer);
		if(buffer == 'a' || buffer == '2' || buffer == '3' || buffer == '4' || buffer == '5' || buffer == '6' || buffer == '7' || buffer == '8' || buffer == '9' || buffer == '0' || buffer == 'j' || buffer == 'q' || buffer == 'k' || buffer == 'd' )
		{
			myCards[i] = buffer;
			i++;
		}
	}while (buffer != 'd');
	*/

	printf("What player are you? (the player who starts is player 1): ");
	scanf("%i", &player);


	while(1)
	{
		//if (feof(stdin))
		//{
		//	clear();
		//}

		clear();

		printCards();
		printf("What would you like to do?: ");
		scanf("%c", &lc);

		if (lc == 'p')
		{
			//printCards();
		}
		else if (lc == 'a')
		{
			addCards();
		}
		else if (lc == 'r')
		{
			removeCards();
		}
		else if (lc == 'o')
		{
			order();
		}
		else if (lc == 'c')
		{
			printf("\n%i\n", cardCount());
		}
		else if (lc == 'q')
		{
			return 0;
		}
		else if (lc == 't')
		{
			turnPlus();
		}
		else if (lc == '-')
		{
			turn--;
			printf("Turn: %i", turn)
		}
	}

	printf("exit\n");
	return 0;

}



