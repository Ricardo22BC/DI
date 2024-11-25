package com.example.catalogactivity;

import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.PorterDuff;
import android.graphics.PorterDuffXfermode;
import android.graphics.Rect;
import android.graphics.RectF;
import android.os.Bundle;
import android.widget.ImageView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import com.squareup.picasso.Picasso;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_detail);

        ImageView imageView = findViewById(R.id.imagen);

        Picasso.get()
                .load(R.drawable.imagen1)
                .transform(new com.squareup.picasso.Transformation() {
                    @Override
                    public Bitmap transform(Bitmap source) {
                        // Redondear la imagen
                        // Aseguramos que la imagen será redonda
                        int diameter = Math.min(source.getWidth(), source.getHeight());
                        Bitmap output = Bitmap.createBitmap(diameter, diameter, Bitmap.Config.ARGB_8888);
                        Canvas canvas = new Canvas(output);

                        final Paint paint = new Paint();
                        final Rect rect = new Rect(0, 0, diameter, diameter);
                        paint.setAntiAlias(true);  // Asegura que el borde sea suave

                        // Dibuja un círculo recortado
                        canvas.drawCircle(diameter / 2, diameter / 2, diameter / 2, paint);

                        // Recorta la imagen dentro del círculo
                        paint.setXfermode(new PorterDuffXfermode(PorterDuff.Mode.SRC_IN));
                        canvas.drawBitmap(source, new Rect(0, 0, source.getWidth(), source.getHeight()), rect, paint);

                        source.recycle();  // Liberar la memoria del bitmap original

                        return output;  // Devuelve la imagen redonda
                    }

                    @Override
                    public String key() {
                        return "circleTransformation()";  // Identificador para la transformación
                    }
                })
                .into(imageView);
    }
}