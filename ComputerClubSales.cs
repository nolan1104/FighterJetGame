
namespace ComputerClubSales
{
    internal class Program
    {
        static void Main(string[] args)
        {
            const decimal caseSalePrice = 12.00m;   // Total sales price
            const decimal caseCost = 7.00m;         // Price of each case
            const int numberOfBarsPerCase = 15;     // Didn't need to use this variable
            const decimal commissionRate = 0.15m;   // 15% commission rate



            // Get the club name
            Console.WriteLine("Hello, what is your club name?");
            string clubName = Console.ReadLine();

            // Get the number of cases sold
            Console.WriteLine("How many cases of candy have you sold?");
            int casesSold = GetNumberOfCases();

            decimal calculatedSales = caseSalePrice * casesSold;                        // Calculated sales
            decimal calculatedCost = caseCost * casesSold;                              // Calculated cost
            decimal commission = calculatedSales * commissionRate;                      // Commission
            decimal netProceeds = calculatedSales - calculatedCost - commission;        // Net Proceeds

            // Fancy display
            Console.WriteLine();
            Console.WriteLine("--------------------------------------------------------------------------------------------------------");
            Console.WriteLine();
            // Display the results
            Console.WriteLine($"The {clubName} computer club produced ${calculatedSales} from their candy sales project.");
            Console.WriteLine($"The total cost of the candy was ${calculatedCost}.");
            Console.WriteLine($"The student government commission amount was {commission:C}.");
            Console.WriteLine($"The net proceeds were {netProceeds:C}.");

            // Pause the program
            Console.ReadLine();


        }
        // Method to make sure number of cases sold is an positive integer
        public static int GetNumberOfCases()
        {
            string input = Console.ReadLine(); 
            try { 
                int convertedNumber =  Convert.ToInt32(input);
                if (convertedNumber < 0)
                {
                    Console.WriteLine("Number cannot be negative. Please enter a valid number.");
                    return GetNumberOfCases();
                }
                return convertedNumber;
            }
            catch (Exception ex)
            {
                Console.WriteLine("Invalid input. Please enter a valid number.");
                return GetNumberOfCases();
            }
        }
    }
}
