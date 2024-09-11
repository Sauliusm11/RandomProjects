using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace PasswordChecker
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("For using https://haveibeenpwned.com/ checker without having to poke your password in it");
            Console.WriteLine("Enter pass");
            string input = Console.ReadLine();
            string hash = HashHelper.Hash(input);
            Console.WriteLine("Your hash:");
            Console.WriteLine(hash);
            Console.WriteLine("Response:");
            HttpService httpService = new HttpService();
            string response = httpService.GetAsync(hash).Result;
            bool found = false;
            foreach (string line in response.Split("\n".ToCharArray(),StringSplitOptions.RemoveEmptyEntries))
            {
                if (hash.Contains(line.Substring(0,35)))
                {
                    Console.WriteLine("Your password has been found");
                    Console.WriteLine(hash.Substring(0,5)+line);
                    found = true;
                }
            }
            if (!found)
            {
                Console.WriteLine("Password not found in any of the known leaks");
            }
        }

    }
    class HashHelper
    {
        public static string Hash(string input)
        {
            using (SHA1Managed sha1 = new SHA1Managed())
            {
                var hash = sha1.ComputeHash(Encoding.UTF8.GetBytes(input));
                var sb = new StringBuilder(hash.Length * 2);

                foreach (byte b in hash)
                {
                    // can be "x2" if you want lowercase
                    sb.Append(b.ToString("X2"));
                }

                return sb.ToString();
            }
        }
    }
    public class HttpService
    {
        private static HttpClient sharedClient = new HttpClient()
        {
            BaseAddress = new Uri("https://api.pwnedpasswords.com/range/"),
            Timeout = TimeSpan.FromMinutes(0.5)
        };

        public async Task<string> GetAsync(string hash)
        {
            string baseUri = sharedClient.BaseAddress.ToString();
            sharedClient.DefaultRequestHeaders.Add("Add-Padding", "true");
            using (HttpResponseMessage response = await sharedClient.GetAsync(baseUri + hash.Substring(0, 5)))
            { return await response.Content.ReadAsStringAsync(); }
        }
    }
}
