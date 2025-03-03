namespace TaxCalculation
{
    internal class Program
    {
        static void Main(string[] args)
        {
            decimal taxRate = 1.07m;
            
            Console.WriteLine("Enter the amount of the purchase: ");
            decimal input = GetInput();

            decimal purchaseAmount = (input * taxRate);

            Console.WriteLine($"The amount of the purchase is: ${purchaseAmount} due to a 7% tax rate.");

        }

        public static decimal GetInput()
        {
            string input = Console.ReadLine();
            try { return Convert.ToDecimal(input); }
            catch (Exception ex)
            {
                Console.WriteLine("Invalid input. Please enter a valid number.");
                return GetInput();
            }
        }
    }
}
