Trying to redirect printf statements to a UART output.

Followed some of the recommendations from this forum
https://www.openstm32.org/forumthread1346
specifically adding this function

```

/*Called by Core -> syscalls.c with weak linkage
adding this function somewhere in the project (with relevant includes)overwrites the syscalls.c __io__putchar definition
This redirects through the ST Link*/

int __io_putchar(int ch)
{
	  HAL_UART_Transmit(&huart3, (uint8_t *)&ch, 1, 0xFFFF);

	  return ch;
}
```