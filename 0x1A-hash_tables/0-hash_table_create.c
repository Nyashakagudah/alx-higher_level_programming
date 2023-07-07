#include "hash_tables.h"

/**
 * hash_table_create - creates a hash table with a given size
 *
 * @table_size: size of the hash table
 * Return: the created hash table, or NULL if function fails
 */
hash_table_t *hash_table_create(unsigned long int table_size)
{
	hash_table_t *hash_table;
	hash_node_t **buckets;
	unsigned long int i;

	/* Allocate memory for hash table struct*/
	hash_table = malloc(sizeof(hash_table_t));
	if (hash_table == NULL)
		return (NULL);

	/* Allocate memory for array of pointers to hash nodes (buckets)*/
	buckets = malloc(sizeof(hash_node_t *) * table_size);
	if (buckets == NULL)
		return (NULL);

	/* Initialize all buckets to NULL*/
	for (i = 0; i < table_size; i++)
		buckets[i] = NULL;

	/* Set size and array in hash table struct*/
	hash_table->array = buckets;
	hash_table->size = table_size;
	return (hash_table);
}
