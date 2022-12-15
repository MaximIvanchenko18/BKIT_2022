// Макрос: сумма нескольких целых чисел
macro_rules! summa_of_int32 {
    ($( $x:expr ),*) => {
        {
            let mut sum: i32 = 0;
            $(
                sum += $x;
            )*
            sum
        }
    };
}
// Через терминал
fn get_terminal_coefs_into(coefs: &mut Vec<f64>) {
    let mut args: Vec<String> = std::env::args().collect(); // считываем все параметры
    // Параметры начинаются с индекса 1, потому что 0 - имя программы
    // Введем массив из имен коэффициентов для удобства
    let coef_names = [String::from("A"), String::from("B"), String::from("C")];
    for i in 1..4 {
        if i < args.len() {
            loop {
                match args[i].trim().parse::<f64>() {
                    Ok(value) => {
                        break coefs.push(value);
                    }
                    Err(_) => {
                        println!("Введите коэффициент {} заново!", coef_names[i-1]);
                        std::io::stdin().read_line(&mut args[i]).expect("Ошибка ввода!");
                        continue
                    }
                }
            }
        }
        else {
            let mut input: String = String::new(); // Строка для ввода
            loop {
                println!("Введите коэффициент {}:", coef_names[i-1]);
                input = String::new();
                std::io::stdin().read_line(&mut input).expect("Ошибка ввода!"); // Ввод
                match input.trim().parse::<f64>() {
                    Ok(value) => {
                        break coefs.push(value);
                    }
                    Err(_) => {
                        print!("Неверно! ");
                        continue
                    }
                }
            }
        }
    }
}

// Через консоль
fn get_coef(message: &String) -> f64{
    let mut input = String::new();
    loop {
        println!("{}", message);
        std::io::stdin().read_line(&mut input).expect("Ошибка ввода");
        match input.trim().parse::<f64>(){
            Ok(value) => {
                break value;
            }
            Err(_) => {
            println!("Неверный формат ввода!");
            continue;
            }
        }
    }
}

fn solution(a: f64, b: f64, c: f64) -> Vec<f64>{
    let mut result: Vec<f64> = Vec::new();
    let diskr: f64 = b.powf(2.0) - 4.0*a*c;
    if diskr == 0f64 {
        result.push(-b/(2.0*a));
    }
    else if diskr > 0f64 {
        result.push((-b-diskr.sqrt())/(2.0*a));
        result.push((-b+diskr.sqrt())/(2.0*a));
    }
    return result;
}

fn main() {
    // Ввод коэффициентов из консоли
    /* let a: f64 = get_coef(&String::from("Введите коэффициент A:"));
    let b: f64 = get_coef(&String::from("Введите коэффициент B:"));
    let c: f64 = get_coef(&String::from("Введите коэффициент C:"));
    // Нахождение решения
    let solution = solution(a, b, c); */

    // Ввод коэффициентов из терминала
    let mut coefs: Vec<f64> = Vec::new();
    get_terminal_coefs_into(&mut coefs);
    // Нахождение решения
    let solution = solution(coefs[0], coefs[1], coefs[2]);

    // Вывод результата
    match solution.len() {
        0 => println!("Нет решений!"),
        1 => println!("Одно решение уравнения: {:.5}", solution[0]),
        2 => println!("Два решения уравнения: {:.5} и {:.5}", solution[0], solution[1]),
        _ => println!("Что-то пошло не так!")
    }

    // Проверка макроса
    println!("Сумма чисел 1, 3, 5, 7 равна:");
    println!("{}", summa_of_int32!(1, 3, 5, 7));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_summa_of_int32() {
        assert_eq!(summa_of_int32!(1,3,5,7), 16);
    }
    #[test]
    fn test_solution_2_ans() {
        assert_eq!(solution(1.0, 0.0, -4.0), vec![-2.0, 2.0]);
    }
    #[test]
    fn test_solution_1_ans() {
        assert_eq!(solution(1.0, -2.0, 1.0), vec![-1.0]); // намеренно ставлю -1
    }
}
